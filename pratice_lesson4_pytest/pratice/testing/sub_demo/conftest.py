import pytest

#默认就是function
@pytest.fixture()
def connectDB():
    print("sub_demo下的连接数据库")
