# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from pratice_lesson5_selenium.page_object.page.main import Main


class TestRegister:
    def setup(self):
        self.main = Main()
    def test_register(self):
        assert self.main.goto_register().register()