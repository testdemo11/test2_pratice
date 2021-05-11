
import pytest

#默认就是function
@pytest.fixture()
def connectDB():
    print("test_demo1中的连接数据库")

def test_a(connectDB):
    print("test a")

class TestA:
    def test_b(self,connectDB):
        print("test b")