# -*- coding:utf-8 -*-
__author__ = 'Tnew'

import pytest
import yaml


class TestDemo:
    @pytest.mark.parametrize("env",yaml.safe_load(open("./env.yml")))
    def test_demo(self,env):
        if "test" in env:
            print("这是测试环境")
            print(env)
            print("测试地址是："+ env["test"])
            # print(yaml.safe_load(open("./env.yml"))
        elif "dev" in env:
            print("这是开发环境")
            print(env)
            print("开发地址是：" + env["dev"])

    def test_yaml(self):
        print(yaml.safe_load(open("./env.yml")))