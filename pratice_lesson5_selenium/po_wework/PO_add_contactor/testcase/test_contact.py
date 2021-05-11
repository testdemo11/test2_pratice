# -*- coding:utf-8 -*-
__author__ = 'Tnew'

import pytest

from pratice_lesson5_selenium.po_wework.PO_add_contactor.page.main_page import MainPage


class TestContact:
    def setup(self):
        self.mainpage = MainPage()

    @pytest.mark.parametrize('username, account, phonenum', open('../data/contact.yaml', encoding='utf-8'))
    def test_member(self, username, account, phonenum):
        page = self.mainpage.goto_add_member()
        page.add_member(username, account, phonenum)
        names = page.get_member()
        assert username in names
