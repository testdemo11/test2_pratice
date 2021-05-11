# -*- coding:utf-8 -*-
__author__ = 'Tnew'

import pytest
import requests


class TestToken:
    #正向测试token:成功
    def test_get_token(self):
        """
        获取access_token
        https://work.weixin.qq.com/api/doc/90000/90135/91039
        :return:
        """
        #第一种方式
        # #定义凭证
        # corpid = "wwca233d5d5e521b32"
        # corpsecret = "d8ZdcI76eHMi2oL2qJRA_VcwBUjOQoG-YjvAJ4RJF_o"
        # #去企业微信的接口文档里获取
        # url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        # r = requests.get(url)
        # print(r.json())

        #第二种方式
        # 定义凭证
        corpid = "wwca233d5d5e521b32"
        corpsecret = "d8ZdcI76eHMi2oL2qJRA_VcwBUjOQoG-YjvAJ4RJF_o"
        params = {
            "corpid":corpid,
            "corpsecret": corpsecret
        }
        # 去企业微信的接口文档里获取
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        r = requests.get(url,params=params)
        print(r.json())
        token = r.json()["access_token"]
        print(token)
        assert r.status_code == 200
        assert r.json()['errmsg'] == 'ok'

    #异常无法获取token
    @pytest.mark.parametrize('corp_id, corp_secret, errmsg',[
        ["wwca233d5d5e521b32",'d8ZdcI76eHMi2oL2qJRA_VcwBUjOQoG-YjvAJ4RJF_o','ok'],
        [None,'d8ZdcI76eHMi2oL2qJRA_VcwBUjOQoG-YjvAJ4RJF_o','corpid missing'],
        ["wwca233d5d5e521b32",None,'corpsecret missing'],
        ["wwca233d5d5e521b45",'d8ZdcI76eHMi2oL2qJRA_VcwBUjOQoG-YjvAJ4RJF_o','invalid corpid'],
        ["wwca233d5d5e521b32",'e8ZdcI76eHMi2oL2qJRA_VcwBUjOQoG-YjvAJ4RJF_o','invalid credential'],
        ["ww876064acebf0fa32","A7LgEhs_Ty_dYXO9BcgY04PJBdawQ6JPzxNQJpv9Yxc",'invalid corpid']
    ])
    def test_token(self,corp_id, corp_secret, errmsg):
        """
        正向验证：ok
        异常逻辑的验证
        1 不传企业ID
        2 不传secret
        3 错误的id
        4 错误的secret
        5 不匹配的id和secret
        :return:
        """
        params = {
            "corpid": corp_id,
            "corpsecret": corp_secret
        }
        # 去企业微信的接口文档里获取
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        r = requests.get(url, params=params)
        print(r.json())
        print(r.json()['errmsg'])
        # token = r.json()["access_token"]
        # print(token)
        print(r.status_code)
        assert r.status_code == 200
        assert errmsg in r.json()['errmsg']