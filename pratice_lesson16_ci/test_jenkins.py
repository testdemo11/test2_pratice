# -*- coding:utf-8 -*-
__author__ = 'Tnew'

import requests
import json

# def test_jenkins():
#         # # 远程调用jenkins api查询任务状态
#         # url = 'http://tnew:1234@192.168.42.130:8080/job/test/1/api/json'
#         # r = requests.get(url)
#         # print(r.text)
#         # print(json.dumps(r.json(), indent=2))
#         #
#         # # 远程调用jenkins api返回最新任务编号
#         # url = 'http://tnew:1234@192.168.42.130:8080/job/test/lastBuild/buildNumber'
#         # r = requests.get(url)
#         # print(r.text)
#         # print(json.dumps(r.json(), indent=2))
#
#         #远程调用jenkins api启动任务，post方法，'http://tnew:1234@192.168.42.130:8080/job/test/build;
#         # jenkins远程跨域请求默认碎片生成器保护，所以post请求可能需要添加相关信息，有现成的封装好的方法调用jenkins api
#         #封装的jenkins api接口
#     url = 'http://192.168.42.130:8080'
#     username = 'tnew'  # jenkins的用户名
#     password = 1234  # jenkins的密码
#     jk = Jenkins(url,username,password,useCrumb=True)
#     print(jk);
from pratice_lesson16_ci.jenkins_demo import JenkinsDemo


class TestJenkinsDemo:
    def test_jenkins(self):
        self.jk = JenkinsDemo('test')
        self.jk.run()
