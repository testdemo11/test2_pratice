from typing import List

import pytest
import yaml

"""
Pytest学习之fixture作用范围（scope）
fixture作用范围
fixture里面有个scope参数可以控制fixture的作用范围:session > module > class > function
- function 每一个函数或方法都会调用
- class  每一个类调用一次，一个类可以有多个方法
- module，每一个.py文件调用一次，该文件内又有多个function和class
- session 是多个文件调用一次，可以跨.py文件调用，每个.py文件就是module

https://www.cnblogs.com/nuonuozhou/p/10429701.html

"""
def pytest_collection_modifyitems(session: "Session", config: "Config", items: List["Item"]) -> None:
    for item in items:
        print(item.name)
        print(item._nodeid)
        #测试用例的名字
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        #测试用例的路径
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        if 'login' in item.nodeid:
            item.add_marker(pytest.mark.login)
    # items.reverse()

#添加一个命令行参数
def pytest_addoption(parser: "Parser", pluginmanager: "PytestPluginManager") -> None:
    mygroup = parser.getgroup('hogwarts') #group将下面所有的option都展示在这个group下
    mygroup.addoption("--env", #注册一个命令行选项
                      default= 'test', #参数的默认值
                      # dest = 'env', #存储的变量
                      help = 'set your run env'#帮助提示参数的描述信息

    )
@pytest.fixture(scope='session')
def cmdoption(request):
    env = request.config.getoption('--env', default='test')
    if env == 'test':
        print('test环境')
        data_path = 'datas/test/datas.yaml'
    elif env == 'dev':
        print('dev环境')
        data_path = 'datas/dev/datas.yaml'
    datas = yaml.safe_load(open(data_path))
    return env,datas