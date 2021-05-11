#conftest是公共的方法，执行测试用例之前都来调用它


import pytest


#默认就是function，session可以跨不同的py文件
# @pytest.fixture(scope="session")
# def connectDB():
#     print("连接数据库操作")
#     yield
#     print("断开数据库连接")
from pratice_lesson4_pytest.pratice.demo.calc import Calculator


@pytest.fixture(scope="class")
def get_calc():
    print("开始计算")
    calc = Calculator()
    return calc
