# -*- coding:utf-8 -*-
__author__ = 'Tnew'

"""
指定某个app -vv 详细日志

adb shell monkey -p com.tencent.wework -vv --pct-touch 10 500

"""

from appium import webdriver


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