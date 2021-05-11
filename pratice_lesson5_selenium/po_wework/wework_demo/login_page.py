# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pratice_lesson5_selenium.po_wework.wework_demo.register_page import RegisterPage


class LoginPage:
    def __init__(self,driver:WebDriver):
        self.driver = driver
    def scan(self):
        """
        扫码
        :return:
        """
        pass


    def goto_register(self):
        self.driver.find_element(By.CSS_SELECTOR,'.login_registerBar_link').click()
        return RegisterPage(self.driver)