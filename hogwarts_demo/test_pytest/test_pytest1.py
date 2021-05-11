# -*- coding:utf-8 -*-
__author__ = 'Tnew'

import pytest


def inc(x):
    return x + 1

@pytest.mark.parametrize('a,b',[
    (1,2),
    (10,20),
    ('a','a1')
])
def test_answer(a,b):
    assert inc(a) == b

@pytest.fixture()
def login():
    print("登录操作")
    username = 'jerry'
    return username

class TestDemo:
    def test_a(self,login):
        print(f"a  username = {login}")
    def test_b(self):
        print('b')
    def test_c(self,login):
        print(f"c  username = {login}")


if __name__ == '__main__':
    pytest.main(['test_pytest1.py::TestDemo::test_c','-v'])
