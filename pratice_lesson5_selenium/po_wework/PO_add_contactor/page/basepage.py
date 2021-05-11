# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    base_url = ''

    def __init__(self, driver: WebDriver = None):
        if self.driver == None:
            # 复用浏览器，设置option
            option = Options()
            option.debugger_address = '127.0.0.1:9228'
            self.driver = webdriver.Chrome(options=option)
            self.driver.implicitly_wait(3)
        else:
            self.driver = driver
        if self.base_url != '':
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

    def find(self, locator, value):
        return self.driver.find_element(locator, value)

    def finds(self, locator, value):
        return self.driver.find_elements(locator, value)

    def wait(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
