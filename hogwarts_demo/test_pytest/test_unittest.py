# -*- coding:utf-8 -*-
__author__ = 'Tnew'
"""
unittest 单元测试，python内置的标准库
覆盖类型：
语句覆盖，条件覆盖，判断覆盖，路径覆盖

编写规则：(类名驼峰命名，TestStringMethods)
import unittest
继承unittest.TestCase
函数以test_命名

def demo_method(a,b,x):
    if a >1 and b ==0:
        x = x /a
    if a == 2 or x>1:
        x = x+1
    return x

"""
import unittest

class TestStringMethods(unittest.TestCase):
    #setUp和tearDown方法是在每条测试用例前后分别调用的方法
    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")

    #setupClass和teardownClass是在整个类的前后分别调用的方法
    @classmethod
    def setUpClass(cls) -> None:
        print("setup class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown class")

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
