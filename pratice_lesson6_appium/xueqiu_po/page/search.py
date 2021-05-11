# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from pratice_lesson6_appium.xueqiu_po.basepage import BasePage


class Search(BasePage):
    def search(self,data):
        self._params["value"] = data
        self.step('../page/search.yaml')
        assert True