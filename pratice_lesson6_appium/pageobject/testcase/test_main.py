# -*- coding:utf-8 -*-
__author__ = 'Tnew'

import pytest
import yaml

from pratice_lesson6_appium.pageobject.page.app import App
from pratice_lesson6_appium.pageobject.testcase.test_base import TestBase


class TestMain(TestBase):
    # @pytest.mark.parametrize("value1,value2",yaml.safe_load(open('../testcase/testdata.yaml')))
    def test_main(self):

        self.app.start().main().goto_search()
        # print(value1)
        # print(value2)

    def test_windows(self):

        self.app.start().main().goto_windows()