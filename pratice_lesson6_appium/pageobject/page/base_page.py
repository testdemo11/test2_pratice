# -*- coding:utf-8 -*-
__author__ = 'Tnew'

import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    # _driver:WebDriver
    _black_list = [(By.ID,'iv_close')]
    def __init__(self,driver:WebDriver=None):
        self._driver = driver

    def find(self,by,locator):
        try:
            element = self._driver.find_element(by,locator)
            return element
        except:
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    break
            return self.find(by,locator)

    def steps(self,path):
        with open(path) as f:
            steps = yaml.safe_load(f)
        for step in steps:
            if 'by' in step.keys():
               element = self.find(step['by'],step['locator'])
            if 'action' in step.keys():
                action = step['action']
                if action == 'click':
                    element.click()

