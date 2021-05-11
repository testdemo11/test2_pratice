# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from typing import List

import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pratice_lesson6_appium.xueqiu_po.page.wrapper_class import WrapperBlack
from pratice_lesson6_appium.xueqiu_po.page.wrapper_decorated import logit


class BasePage:
    _params = {}
    _black_list = [(MobileBy.XPATH,'//*[@resource-id="com.xueqiu.android:id/iv_close"]')]

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    @WrapperBlack(logfile='black.log')
    def find(self, by, locator=None):
        return self.driver.find_element(by, locator)


    def finds(self,by,locator=None):
        return self.driver.find_elements(by,locator)

    def find_click(self,by,locator):
        return self.find(by,locator).click()

    def send(self, by, locator,value):
        return self.find(by, locator).send_keys(value)

    def swipe_click(self, text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable(new UiSelector().'
                                        'scrollable(true).instance(0)).'
                                        f'scrollIntoView(new UiSelector().text("{text}").'
                                        'instance(0));').click()

    def wait(self, by, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((by, locator)))

    def step(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            steps: List[dict] = yaml.safe_load(f)
        for step in steps:
            if step['action'] == "click":
                self.find_click(step['by'], step['locator'])
            elif step['action'] == "swipe_click":
                self.swipe_click(step['locator'])
            elif step['action'] == 'send':
                content: str = step['value'] #"{value}"
                for param in self._params:
                    """self._params["value"] = value"""
                    content = content.replace("{%s}" % param, self._params[param])
                self.send(step['by'], step['locator'],content)
            elif step['action'] == 'wait':
                self.wait(step['by'], step['locator'])
