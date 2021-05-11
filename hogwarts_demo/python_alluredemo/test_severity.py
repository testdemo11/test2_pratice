# -*- coding:utf-8 -*-
__author__ = 'Tnew'

import allure
import pytest


@allure.severity(allure.severity_level.CRITICAL)
def test_with_critical():
    pass

@allure.severity(allure.severity_level.NORMAL)
def test_with_normal():
    pass

@allure.severity(allure.severity_level.TRIVIAL)
def test_with_trivial():
    pass

@allure.severity(allure.severity_level.NORMAL)
class TestClassWithNormalSeverity():
    def test_inside_the_normal_severity_test_class(self):
        pass

    @allure.severity(allure.severity_level.CRITICAL)
    def test_inside_the_normal_severity_test_class_with_overriding_critical_severity(self):
        pass

if __name__ == '__main__':
    pytest.main()
