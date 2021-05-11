# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from selenium.webdriver.common.by import By

from pratice_lesson5_selenium.page_object.page.base_page import BasePage
from pratice_lesson5_selenium.page_object.page.register import Register


class Login(BasePage):
    def scan(self):
        pass
    def goto_register(self):
        self.find(By.CSS_SELECTOR,".login_registerBar_link").click()
        return Register(self._driver)