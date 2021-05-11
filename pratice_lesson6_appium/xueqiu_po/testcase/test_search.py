# -*- coding:utf-8 -*-
__author__ = 'Tnew'

import pytest
import yaml

from pratice_lesson6_appium.xueqiu_po.app import App



class TestSearch:
    def setup(self):
        self.app = App()
    @pytest.mark.parametrize('data',['alibaba','茅台','xiaomi'])
    # @pytest.mark.parametrize('data',yaml.safe_load(open('../datas/data.yaml',encoding='utf-8')))
    def test_search(self,data):
        self.app.start().goto_main().goto_market().goto_search().search(data)