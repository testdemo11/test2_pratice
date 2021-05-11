# -*- coding:utf-8 -*-
__author__ = 'Tnew'
"""


注意自动打卡有两个动态页面加载，定位需要等10s，加'settings[waitForIdleTimeout]': 0,可减少等待时间，提高效率
"""
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.mobile import Mobile

"""
adb shell
dumpsys window|grep mCurrent 得到activity

com.tencent.wework/com.tencent.wework.launch.WwMainActivity
"""
class TestWework:
    def setup(self):
        desire_caps = {
            "platformName": 'android',
            "deviceName": '127.0.0.0:7555',
            "appPackage": 'com.tencent.wework',
            "appActivity": 'com.tencent.wework.launch.WwMainActivity',
            "noReset": 'true',
            'settings[waitForIdleTimeout]': 0,
            "ChromedriverExecutable": "D:/Study/Automation_Tester_Guide/Lesson6_appium/chromedriver"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_wework(self):
        #点击工作台
        self.driver.find_element(MobileBy.XPATH,'//*[@text="工作台"]').click()
        #滑动到打卡并点击
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        f'scrollIntoView(new UiSelector().text("打卡").'
                                                        'instance(0));').click()
        #点击外出打卡
        # self.driver.find_element_by_id("com.tencent.wework:id/ghc").click()
        self.driver.find_element_by_xpath("//*[@text='外出打卡']").click()

        #点击包含次外出文字
        self.driver.find_element_by_xpath('//*[contains(@text,"次外出")]').click()

        #找到打卡成功的text并判断断言
        element = self.driver.find_element_by_id("mn").text
        # element = self.driver.find_element_by_id("com.tencent.wework:id/mn").text

        # print(element)
        assert '外出打卡成功' == element