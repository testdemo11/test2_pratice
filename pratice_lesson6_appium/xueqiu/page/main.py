# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from pratice_lesson6_appium.xueqiu.page.base_page import BasePage
from pratice_lesson6_appium.xueqiu.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.steps("../page/hangqing.yaml")
        return Market(self._driver)