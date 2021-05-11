# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from appium.webdriver.common.mobileby import MobileBy

from pratice_lesson6_appium.xueqiu_po.basepage import BasePage
from pratice_lesson6_appium.xueqiu_po.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.find_click(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']")
        self.step('../page/main_menu.yaml')
        return Market(self.driver)