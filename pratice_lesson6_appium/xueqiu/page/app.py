# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from appium import webdriver

from pratice_lesson6_appium.xueqiu.page.base_page import BasePage
from pratice_lesson6_appium.xueqiu.page.main import Main


class App(BasePage):
    def start(self):
        _package = 'com.xueqiu.android'
        _activity = '.view.WelcomeActivityAlias'
        if self._driver is None:
            desire_caps ={}
            desire_caps["platformName"] = 'android'
            desire_caps["deviceName"] = '127.0.0.1:7555'
            desire_caps["appPackage"] = _package
            desire_caps["appActivity"] = _activity
            # desire_caps["noReset"] = "true"
            # desire_caps['dontStopAppOnReset'] = 'true'
            # desire_caps['skipDeviceInitialization'] = 'true'
            # desire_caps['unicodeKeyBoard'] = 'true'
            # desire_caps['resetKeyBoard'] = 'true'
            desire_caps['autoGrantPermissions'] = True
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
            self._driver.implicitly_wait(5)
        else:
            self._driver.start_activity(_package,_activity)

        return self

    def main(self):
        return Main(self._driver)
