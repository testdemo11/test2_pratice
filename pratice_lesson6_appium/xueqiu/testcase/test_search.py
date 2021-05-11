# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from pratice_lesson6_appium.xueqiu.page.app import App


class TestSearch:
    def test_search(self):
        App().start().main().goto_market().goto_search().search("jd")