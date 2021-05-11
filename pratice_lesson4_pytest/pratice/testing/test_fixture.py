import pytest

#加上autouse后，不需要传入fixture也会调用
@pytest.fixture()
def login():
    print("登录操作")
    print("获取token")
    username = "tom"
    password = "123456"
    token = "token124sdjfd"
    #yield 激活fixture的teardown功能,也可以返回值
    #yield相当于return，返回数据直接跟在yield后面
    yield [username,password,token]
    print("注销操作")



#需要提前登录
#第一种方法：在测试用例中传入fixture方法名
def test_case1(login):
    #获取fixture方法的返回值，直接调用fixture方法名
    print(f"用户信息为：{login}")
    print("test case 1")
#不需要提前登录
def test_case2(connectDB):
    print("test case 2")

#需要提前登录
def test_case3():
    print("test case 3")

#需要提前登录
#第二种方法：@pytest.mark.usefixtures("login")
@pytest.mark.usefixtures("login")
def test_case4():
    print(f"用户信息为：{login}")
    print("test case 4")