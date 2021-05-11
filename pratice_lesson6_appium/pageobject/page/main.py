# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from selenium.webdriver.common.by import By

from pratice_lesson6_appium.pageobject.page.base_page import BasePage


class Main(BasePage):
    def goto_search(self):
        self.steps("../page/steps.yaml")

    def goto_windows(self):
        self.find(By.ID,'post_status').click()
        self.find(By.ID,'tv_search').click()

