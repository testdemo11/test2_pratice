# -*- coding:utf-8 -*-
__author__ = 'Tnew'

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import assert_that, close_to


class TestDW:
    def setup(self):
        desire_caps = {}
        desire_caps["platformName"] = 'android'
        desire_caps["deviceName"] = '127.0.0.1:7555'
        desire_caps["appPackage"] = 'com.xueqiu.android'
        desire_caps["appActivity"] = '.view.WelcomeActivityAlias'
        desire_caps["noReset"] = "true"
        # desire_caps['dontStopAppOnReset'] = 'true'
        desire_caps['skipDeviceInitialization'] = 'true'
        desire_caps['unicodeKeyBoard']='true'
        desire_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/action_close").click()
        # self.driver.quit()
    @pytest.mark.parametrize('searchkey,type,price',[
        ('阿里巴巴','BABA',250),('小米集团-W','01810',26)
    ])
    def test_search(self,searchkey,type,price):
        """
        打开雪球，搜索阿里巴巴或小米集团-W
        搜索第一个结果查找代号BABA的价格，点击取消，
        :return:
        """
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/name']").click()
        ele = self.driver.find_element(MobileBy.XPATH,f"//*[@text='{type}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        current_price = float(ele.text)
        # expect_price=250
        assert_that(current_price,close_to(price,price*0.1))

    # def test_search1(self):
    #     """
    #     打开雪球，搜索阿里巴巴或小米集团-W
    #     搜索第一个结果查找代号BABA的价格，点击取消，
    #     :return:
    #     """
    #     self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/tv_search").click()
    #     self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/search_input_text").send_keys('阿里巴巴')
    #     self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/name']").click()
    #     ele = self.driver.find_element(MobileBy.XPATH,"//*[@text='BABA']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
    #     current_price = float(ele.text)
    #     expect_price=250
    #     assert_that(current_price,close_to(expect_price,expect_price*0.1))