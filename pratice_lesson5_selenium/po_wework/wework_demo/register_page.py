# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RegisterPage:
    def __init__(self,driver:WebDriver):
        self.driver = driver

    def register(self):
        self.driver.find_element(By.ID,'corp_name').send_keys('tnewtao')
        self.driver.find_element(By.ID,'manager_name').send_keys('sihan')
        self.driver.find_element(By.ID,'register_tel').send_keys('15245128125')
        self.driver.find_element(By.ID,'submit_btn').click()
        return True


