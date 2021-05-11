# -*- coding:utf-8 -*-
__author__ = 'Tnew'

#首页
from selenium import webdriver
from selenium.webdriver.common.by import By

from pratice_lesson5_selenium.po_wework.wework_demo.login_page import LoginPage
from pratice_lesson5_selenium.po_wework.wework_demo.register_page import RegisterPage


class IndexPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")

    def goto_register(self):
        """
        进入到注册页面
        1 click register button
        2 return RegisterPage
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR,'.index_head_info_pCDownloadBtn').click()
        return RegisterPage(self.driver)

    def goto_login(self):
        """
        进入到登录页面
        1 click login button
        2 return LoginPage
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR,'.index_top_operation_loginBtn').click()
        return LoginPage(self.driver)