# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from appium.webdriver.common.mobileby import MobileBy

from pratice_lesson6_appium.xueqiu.page.search import Search
from pratice_lesson6_appium.xueqiu_po.basepage import BasePage


class Market(BasePage):
    def goto_search(self):

        self.step('../page/market.yaml')
        return Search(self.driver)
