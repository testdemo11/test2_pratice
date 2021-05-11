import pytest


@pytest.mark.parametrize('name',['哈利','博波特'])
def test_hk(name):
    print(name)

def test_login():
    pass

def test_login1():
    print('login')

def test_search():
    pass

def test_env(cmdoption):
    # print(cmdoption)
    env,datas = cmdoption
    host = datas['env']['host']
    port = datas['env']['port']
    url = str(host)+':'+str(port)
    print(url)