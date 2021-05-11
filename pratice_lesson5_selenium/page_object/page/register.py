# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from selenium.webdriver.common.by import By

from pratice_lesson5_selenium.page_object.page.base_page import BasePage


class Register(BasePage):
    def register(self):
        self.find(By.ID,"corp_name").send_keys("hello")
        self.find(By.ID,"manager_name").send_keys("tom")
        return True
