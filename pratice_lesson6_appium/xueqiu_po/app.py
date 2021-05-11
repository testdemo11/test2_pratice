# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from pratice_demo.pratice_wework_add_contactor_po_appium.page.basepage import BasePage
from pratice_lesson6_appium.xueqiu_po.page.main import Main


class App(BasePage):
    _package = 'com.xueqiu.android'
    _activity = '.view.WelcomeActivityAlias'
    """
    打开雪球，并返回到主页
    """
    def start(self):
        if self.driver is None:
            desire_caps = {
                "platformName": 'android',
                "deviceName": '127.0.0.0:7555',
                "appPackage": self._package,
                "appActivity": self._activity,
                "noReset": 'true',
                'settings[waitForIdleTimeout]': 0,
                "ChromedriverExecutable": "D:/Study/Automation_Tester_Guide/Lesson6_appium/chromedriver"
            }
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver.start_activity(self._package,self._activity)
        return self

    def goto_main(self):
        return Main(self.driver)