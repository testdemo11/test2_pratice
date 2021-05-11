# -*- coding:utf-8 -*-
__author__ = 'Tnew'

import yaml
from appium import webdriver

from pratice_lesson6_appium.pageobject.page.base_page import BasePage
from pratice_lesson6_appium.pageobject.page.main import Main


class App(BasePage):
    _package = 'com.xueqiu.android'
    _activity = '.view.WelcomeActivityAlias'

    def start(self):
        if self._driver is None:
            desire_caps={}
            desire_caps["platformName"] = 'android'
            desire_caps["deviceName"] = '192.168.216.101:5555'
            desire_caps["appPackage"] = self._package
            desire_caps["appActivity"] = self._activity
            desire_caps["noReset"] = "true"
            desire_caps['udid'] = yaml.safe_load(open('../page/configuration.yaml'))['caps']['udid']
            # desire_caps['dontStopAppOnReset'] = 'true'
            # desire_caps['skipDeviceInitialization'] = 'true'
            desire_caps['unicodeKeyBoard'] = 'true'
            desire_caps['resetKeyBoard'] = 'true'
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        else:
            self._driver.start_activity(self._package,self._activity)
        self._driver.implicitly_wait(3)
        return self

    def main(self):
        return Main(self._driver)