# -*- coding:utf-8 -*-
__author__ = 'Tnew'
from appium import webdriver
desired_caps = {}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='6.0'
desired_caps['deviceName']='127.0.0.1:7555'
desired_caps['appPackage']='com.android.settings'
desired_caps['appActivity']='com.android.settings.Settings'
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)
driver.quit()

