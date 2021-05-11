# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from pratice_lesson5_selenium.po_wework.wework_demo.index_page import IndexPage


class TestRegister:
    def setup(self):
        self.index = IndexPage()

    def test_register(self):
        assert self.index.goto_login().goto_register().register()