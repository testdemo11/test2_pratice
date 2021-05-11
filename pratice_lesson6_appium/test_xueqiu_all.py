# -*- coding:utf-8 -*-
__author__ = 'Tnew'
# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from time import sleep

import pytest
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import *

"""
常用两种定位方式id, accessibility_id
driver.find_element_by_id(resource-id)
driver.find_element_by_accessibility_id(content-desc)

测试步骤三要素
定位，交互，断言

元素常用方法：
点击方法 element.click()
输入操作： element.send_keys()
设置元素的值：element.set_value()
清除操作：element.clear()
是否可见：element.is_displayed()返回True/False
是否可用：element.is_enabled()返回True/False
是否被选中：element.is_selected()返回True/False
获取属性值：get_attribute()

常用属性：
元素文本：element.text
坐标：element.location {}
尺寸：element.size {}


/ 根节点
// 从匹配的当前节点选择文档中的节点，不考虑他们的位置
. 当前节点
.. 当前节点的父节点
@ 选取属性


Uiautomatorviewer:
uiautomator 定位
通过resourceid定位
new UiSelector().resourceId("id")
通过classname定位
new UiSelector().className("className")
通过content-desc定位
new UiSelector().description(“contenet-des属性”)


new UiSelector().text()
new UiSelector().textContains()
new UiSelector().textStartsWith(“以text文本开头”)
new UiSelector().textMatches("正则表达式")
父子关系定位 childSelector
son = 'resourceId('').childSelector(text("股票"))'
兄弟定位 fromParent
brother = 'resourceId('').fromParent(text("用户"))'

driver.find_element_by_android_uiautomator(表达式).click()

uiautomator实现滚动查找元素
new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("查找的文本").instance(0))
"""
from appium import webdriver
import os
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
        desire_caps['udid'] = '127.0.0.1:7555'
        # desire_caps['udid'] = os.getenv('udid',None)
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        # self.driver = webdriver.Remote("http://192.168.216.2:4444/wd/hub", desire_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_search1(self):
        self.driver.find_element_by_xpath("//*[@text='行情']").click()

    def test_search(self):
        """
        打开雪球app
        点击搜索输入框
        向搜索输入框输入阿里巴巴
        在搜索结果里面选择阿里巴巴，然后进行点击
        获取这支香港阿里巴巴的股价，并判断这只股价的价格>200
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys('阿里巴巴')
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        assert current_price > 200


    def test_search2(self):
        """
        打开雪球app 首页
        定位首页搜索框
        判断搜索框是否可用，并查看name的属性值
        打印搜索框元素的左上角坐标和它的宽高
        向搜索框输入：alibaba
        判断alibaba是否可见
        如果可见，打印搜索成功，不可见，打印搜索失败
        """
        ele_search =  self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(ele_search.text)
        print(ele_search.size)
        print(ele_search.location)
        if  ele_search.is_enabled() == True:
            ele_search.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys('阿里巴巴')
            ele = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            # ele.is_displayed() 布尔值True
            #get_attribute得到的是一个‘true’
            if ele.get_attribute('displayed') == 'true':
                print("搜索成功")
            else:
                print("搜索失败")


    def test_touchaction(self):
        """
        TouchAction().press().moveTo().release().perform()
        :return:
        """
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/title_text' and @text='推荐']").click()
        sleep(3)
        action=TouchAction(self.driver)
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width/2)
        y_start = int(height * 4/5)
        y_end = int(height * 1/5)
        action.press(x=x1,y=y_start).wait(2000).move_to(x=x1,y=y_end).wait(2000).release().perform()


    def test_get_current(self):
        """
        打开雪球
        搜索阿里巴巴
        从搜索结果查找，找到阿里巴巴香港股票的价格
        :return:
        """
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys('阿里巴巴')
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        locator = (MobileBy.XPATH,"//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        current_price = self.driver.find_element(*locator).text
        assert float(current_price)>200


    def test_myinfo(self):
        """
        打开雪球
        点击我的，进入到个人信息页面
        点击登录，进入登录页面
        输入用户名，输入密码
        点击登录
        :return:
        """
        # self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/tab_icon' and @text='我的']").click()
        # self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("帐号密码登录")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("username")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("password")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()


    def test_scroll_find_element(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("关注")').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("茅台").'
                                                        'instance(0));')

    def test_get_attribute(self):

        ele = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        print(ele.get_attribute("resource-id"))


    def test_hamrest(self):
        # assert_that(10,equal_to(10))
        # assert_that(10,close_to(8,2))
        assert_that("contains some string",contains_string("string"))