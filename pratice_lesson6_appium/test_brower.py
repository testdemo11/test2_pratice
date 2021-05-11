# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDW:
    def setup(self):
        desire_caps = {}
        desire_caps["platformName"] = 'android'
        desire_caps["deviceName"] = '192.168.216.101:5555'
        desire_caps["browserName"] = 'Browser'
        # desire_caps["appActivity"] = '.view.WelcomeActivityAlias'
        desire_caps["noReset"] = "true"
        # desire_caps['dontStopAppOnReset'] = 'true'
        # desire_caps['skipDeviceInitialization'] = 'true'
        # desire_caps['unicodeKeyBoard']='true'
        # desire_caps['resetKeyBoard'] = 'true'
        # desire_caps['chromedriverExecutable'] = 'D:/Study/Automation_Tester_Guide/Lesson6_appium/chromedriver'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get("http://m.baidu.com")
        self.driver.find_element_by_id("index-kw").click()
        self.driver.find_element_by_id("index-kw").send_keys("appium")
        search_locator = (By.ID,"index-bn")
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(search_locator))
        self.driver.find_element(*search_locator).click()
