# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _base_url = ''
    def __init__(self,driver:WebDriver=None):
        self._driver =''
        if driver is None:
            self._driver = webdriver.Chrome()
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self,by,locator):
        return self._driver.find_element(by,locator)


# class Login(BasePage):
#     def scan(self):
#         pass
#     def goto_register(self):
#         self.find(By.CSS_SELECTOR,".login_registerBar_link").click()
#         return Register(self._driver)
#
# class Register(BasePage):
#     def register(self):
#         self.find(By.ID,"corp_name").send_keys("hello")
#         self.find(By.ID,"manager_name").send_keys("tom")
#         return True
