

import requests
import yaml
import pystache
from jsonpath import jsonpath
from hamcrest import *
from jsonschema import validate
import json
from requests.auth import HTTPBasicAuth
import base64

class TestDemo:
    def test_get(self):
        r= requests.get("http://httpbin.testing-studio.com/get")
        print(r.status_code)
        print(r.json)
        print(r.text)
        assert r.status_code == 200

    def test_query(self):
        payload = {
            "level":1,
            "name": "tnew"
        }
        r = requests.get("http://httpbin.testing-studio.com/get",params=payload)
        # print(r.text)
        # print(r.headers)
        # assert 'tnew' in r.text
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            "level": 1,
            "name": "tnew"
        }
        r =requests.post(" http://httpbin.testing-studio.com/post",data=payload)
        print(r.text)
        assert r.status_code ==200

    def test_post_file(self):
        url  = "http://httpbin.testing-studio.com/post"
        file = {'file': open('../hogwarts_api/test.txt','rb')}
        r = requests.post(url=url,files=file)
        print(r.text)
        assert r.status_code == 200
    def test_get_header(self):
        headers = {'content-type':'application/json'}
        url = "http://httpbin.testing-studio.com/get"
        r =  requests.get(url=url,headers=headers)
        print(r.headers)
        print(r.headers['content-type']) #application/json
        # assert r.status_code == 200
        assert 'application/json' == r.headers['content-type']

    def test_get_cookie(self):
        # #第一种
        # dict  ={}
        # dict['name'] = 'tnew'
        # cookies = dict
        # 第二种
        cookies = dict(name='tnew')
        #第三种
        # dict={'name':'tnew'}
        # cookies = dict
        url = "http://httpbin.testing-studio.com/get"
        r  = requests.get(url=url,cookies=cookies)
        #响应的内容
        print(r.text)
        print(type(r.text)) #<class 'str'>,所以不能通过想拿到响应的信息，用r.json()的方式
        print(r.headers)  # 注意，r.headers里面没有Cookie
        # print(r.json())
        # print(r.json()['headers']['Cookie'])
        # 请求的头信息
        # print(r.request.headers)
        #请求的头信息
        # print(r.request.headers['Cookie'])

        # print(r.cookies)
        # assert r.status_code == 200
        # assert "name=tnew" in r.request.headers['Cookie']
        assert "name=tnew" in r.json()['headers']['Cookie']

    def test_post_json(self):
        payload = {
            "level": 1,
            "name": "tnew"
        }
        r = requests.post(" http://httpbin.testing-studio.com/post", json=payload)
        print(r.text)
        print(r.json()['json'])
        assert 'tnew' == r.json()['json']['name']

    def test_hogwarts(self):
        url = 'https://home.testing-studio.com/categories.json'
        r = requests.get(url=url)
        print(r.json())
        print(r.json()['category_list']['categories'][0]['name'])
        # assert "开源项目" == r.json()['category_list']['categories'][0]['name']
        #取所有name中的第一个
        assert jsonpath(r.json(),'$..name')[0] == "开源项目"

    def test_hamcrest(self):
        url = 'https://home.testing-studio.com/categories.json'
        r = requests.get(url=url)
        print(r.json())
        print(r.json()['category_list']['categories'][0]['name'])
        # assert "开源项目" == r.json()['category_list']['categories'][0]['name']
        # 取所有name中的第一个
        assert_that(r.json()['category_list']['categories'][0]['name'],equal_to('开源项目'))

    def test_get_login_jsonschema(self):
        url = 'https://testerhome.com/api/v3/topics.json'
        data = requests.get(url=url,params={"limit":'2'}).json()
        print(data)
        schema = json.load(open("../hogwarts_api/topic_schema.json",encoding='utf-8'))
        print(schema)
        validate(data,schema= schema)

    def test_header_cookie(self):
        url = "http://httpbin.testing-studio.com/cookies"
        header = {
            "Cookie":"test",
            "User-Agent":"application/json"
        }
        r = requests.get(url=url,headers= header)
        print(r.request.headers)

    def test_cookies(self):
        url = "http://httpbin.testing-studio.com/cookies"
        header = {
           "User-Agent": "application/json"
        }
        cookies= {"username":"tnew","password":"123456"}
        r = requests.get(url=url, headers=header,cookies = cookies)
        print(r.request.headers)


    def test_oauth(self):
        url = "http://httpbin.testing-studio.com/basic-auth/test/123"
        r = requests.get(url=url,auth = HTTPBasicAuth("test","123"))
        print(r.text)

    def test_encode(self):
        url ="http://127.0.0.1:9999/demo.txt"
        r= requests.get(url=url)
        print(r.text)
        #使用base64来解密,并用json.loads来处理格式
        # res = base64.b64decode(r.content)
        res = json.loads(base64.b64decode(r.content))
        print(res)

