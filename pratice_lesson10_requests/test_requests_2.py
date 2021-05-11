"""
多环境下的接口测试
请求之前，对请求的url进行替换
1 二次封装requests,对请求定制化
2 url改成一个域名
3 使用env配置文件，存放各个环境的配置信息
4 将请求结构体中的url替换成env配置文件中的url
5 env配置文件使用yaml管理

"""
import base64
import json

import pytest
import requests
import yaml


class ApiRequest:
    # env = {
    #         'default':"test",
    #         "test-studio":
    #         {'dev': "127.0.0.1",
    #          'test':'127.0.0.2'}
    #        }
    env = yaml.safe_load(open('./datas/data.yaml',encoding='utf-8'))
    def send(self,data:dict):
        print(self.env['test-studio'][self.env['default']])
        #替换，选择环境
        data['url'] = data['url'].replace("test-studio", self.env["test-studio"][self.env['default']])
        # data['url'] = data['url'].replace("test-studio", "127.0.0.1")
        # data['url'] = str(data['url']).replace("test-studio","127.0.0.1")
        print(data['url'])
        res = requests.request(data['method'],data['url'],headers=data['headers'])
        if data['encoding'] == "base64":
            return json.loads(base64.b64decode(res.content))
        #把加密过后的响应值发给第三方服务，让第三方去做解密然后返回解密过后的信息
        elif data['encoding'] == 'private':
            return requests.post("url", data=res.content)

class TestApiRequest:
    req_data = {
        "method": "get",
        "url": "http://test-studio:9999/demo.txt",
        "headers": None,
        "encoding": "base64"
    }
    def test_send(self):
        self.req = ApiRequest()
        response_data = self.req.send(self.req_data)
        print(response_data)