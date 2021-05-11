# -*- coding:utf-8 -*-
__author__ = 'Tnew'
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Remote
class TestGrid:
    def test_grid(self):
        hub_url = 'http://127.0.0.1:4444/wd/hub'
        capability = DesiredCapabilities.CHROME.copy() #字典的深拷贝，不改变原来的
        capability['platform'] = 'windows'
        for i in range(1,5):
            driver = Remote(command_executor=hub_url,desired_capabilities=capability)
            driver.get('https://www.selenium.dev/downloads/')