# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from pratice_lesson6_appium.xueqiu.page.base_page import BasePage
from pratice_lesson6_appium.xueqiu.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.steps("../page/market.yaml")
        return Search(self._driver)