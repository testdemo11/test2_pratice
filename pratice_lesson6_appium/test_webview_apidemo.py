# -*- coding:utf-8 -*-
__author__ = 'Tnew'

"""
adb shell
pm list packages 拿到手机上当前的package
pm dump com.android.webview|grep version 拿到webview的版本信息
74.0.3729.186
"""

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By


class TestDW:
    def setup(self):
        desire_caps = {}
        desire_caps["platformName"] = 'android'
        desire_caps["deviceName"] = '192.168.216.101:5555'
        desire_caps["appPackage"] = 'io.appium.android.apis'
        desire_caps["appActivity"] = 'io.appium.android.apis.ApiDemos'
        desire_caps["noReset"] = "true"
        # desire_caps['dontStopAppOnReset'] = 'true'
        # desire_caps['skipDeviceInitialization'] = 'true'
        # desire_caps['unicodeKeyBoard']='true'
        # desire_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(5)
        # desire_caps['ChromedriverExecutable']='D:/Study/Automation_Tester_Guide/Lesson6_appium/Appium-windows-1.19.1/resources/app/node_modules/appium/node_modules/appium-chromedriver/chromedriver/win/chromedriver_win32_v2.24.exe'

    def teardown(self):
        self.driver.quit()

    def test_webview(self):
        #第一种
        view = 'Views'
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        f'scrollIntoView(new UiSelector().text("{view}").'
                                                        'instance(0));').click()

        #第二种
        # action = TouchAction(self.driver)
        # window_rect = self.driver.get_window_rect()
        # print(window_rect)
        # width = window_rect['width']
        # height = window_rect['height']
        # x1 = int(width / 2)
        # y_start = int(height * 4 / 5)
        # y_end = int(height * 1 / 5)
        # action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).wait(200).release().perform()
        # self.driver.find_element_by_accessibility_id("Views").click()

        # print(self.driver.contexts)
        webview = "WebView"
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        f'scrollIntoView(new UiSelector().text("{webview}").'
                                                        'instance(0));').click()
        # self.driver.find_element(MobileBy.XPATH,'//*[@text="i has no focus"]').send_keys("this is test")
        # self.driver.find_element(MobileBy.XPATH,'//*[@text="i am a link"]').click()
        # print(self.driver.page_source)

        # print(self.driver.contexts)

        #切换webview上下文
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element(MobileBy.ID,"i_am_a_textbox").send_keys("this is test")
        self.driver.find_element(MobileBy.ID,"i am a link").click()

