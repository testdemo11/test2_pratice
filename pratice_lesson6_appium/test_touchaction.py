# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestTouchAction:
    def setup(self):
        desire_caps = {}
        desire_caps["platformName"] = 'android'
        desire_caps["deviceName"] = '127.0.0.1:7555'
        desire_caps["appPackage"] = 'cn.kmob.screenfingermovelock'
        desire_caps["appActivity"] = 'com.samsung.ui.MainActivity'
        desire_caps["noReset"] = "true"
        # desire_caps['dontStopAppOnReset'] = 'true'
        desire_caps['skipDeviceInitialization'] = 'true'
        desire_caps['unicodeKeyBoard'] = 'true'
        desire_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(10)
    def teardown(self):
        self.driver.quit()

    def test_figure(self):
        """
        手势操作解锁
        :return:
        """
        print("解锁密码")
        action = TouchAction(self.driver)
        action.press(x=118,y=171).move_to(x=360,y=171).move_to(x=604,y=178).move_to(x=596,y=412).move_to(x=596,y=653).release().perform()
        # window_rect = self.driver.get_window_rect()
        # print(window_rect)
        # width = window_rect['width']
        # height = window_rect['height']
        # x1 = int(width / 2)
        # y_start = int(height * 4 / 5)
        # y_end = int(height * 1 / 5)
        # action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).wait(200).release().perform()

