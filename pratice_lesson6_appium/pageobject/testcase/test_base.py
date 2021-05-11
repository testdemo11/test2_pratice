# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from pratice_lesson6_appium.pageobject.page.app import App


class TestBase:
    app = None
    def setup(self):
        self.app = App()