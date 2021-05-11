# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from selenium import webdriver

def test_selenium():
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")