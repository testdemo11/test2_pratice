# -*- coding:utf-8 -*-
__author__ = 'Tnew'

import pytest
import yaml
#使用string "a,b" 使用list ["a","b"]  使用turple("a","b")

# class TestData:
#     @pytest.mark.parametrize(["a","b"],[(10,20),(10,30)])
#     def test_data(self,a,b):
#         print(a+b)



class TestData:
    @pytest.mark.parametrize(("a","b"),yaml.safe_load(open("./demo.yaml")))
    def test_data(self,a,b):
        print(a+b)