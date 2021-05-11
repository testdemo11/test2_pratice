# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from pratice_lesson6_appium.xueqiu.page.base_page import BasePage


class Search(BasePage):
    def search(self,value):
        self._params["value"] = value
        self.steps("../page/search.yaml")