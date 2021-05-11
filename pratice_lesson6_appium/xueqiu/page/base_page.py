# -*- coding:utf-8 -*-
__author__ = 'Tnew'

import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

"""
如果你使用find_element方法，当无法定位到元素的时候，代码会直接抛出异常，导致运行中断，这样就不符合黑名单处理的想法了。
因为黑名单中的元素是一系列可能出现的异常元素的集合，我们的设计思路就是在原本需要定位的元素无法找到的时候，再去黑名单列表中一个一个确认这些异常元素是否出现。
而使用find_elements的时候，不管是否找到，找到几个，都会如实返回而不是报错，这样就可以支持我们进行之后的处理。
如果没找到当前这个黑名单元素，那么就循环去找下一个黑名单中的元素，如果找到了，那么就进行之前设计好的操作（比如你代码中的click()）

"""
class BasePage:
    _black_list = [(By.ID,"image_cancel")]
    _error_cont =0
    _error_max=10
    _params={}
    def __init__(self,driver:WebDriver=None):
        self._driver = driver

    def find(self, by, locator=None):
        try:
            #承接元组或者非元组
            element = self._driver.find_elements(*by) if isinstance(by, tuple) else self._driver.find_element(by, locator)
            self._error_cont = 0
            return element
        except Exception as e:
            #如果没找到会陷入死循环
            self._error_cont +=1
            if self._error_cont >= self._error_max:
                raise e
            #取出弹框的元素，进行点击
            for black in self._black_list:
               elements = self._driver.find_elements(*black)
               if len(elements) > 0:
                   elements[0].click()
                   return self.find(by, locator)
            raise e

    def send(self,value, by, locator=None):
        try:
            self.find(by, locator).send_keys(value)
            self._error_cont = 0
        except Exception as e:
            self._error_cont +=1
            if self._error_cont >= self._error_max:
                raise e
            """ 循环遍历，但是有个问题，如果弹窗没有的话就会陷入一直查找的死循环，因此需要设置一个错误次数， 这里要是没有的话len=0，就不会进入if语句中，
            　　  就没有办法从for循环中出来"""
            for black in self._black_list:
               elements = self._driver.find_elements(*black)
               if len(elements) > 0:
                   elements[0].click()
                   return self.send(value, by, locator)
            raise e

    def steps(self,path):
        with open(path,encoding="utf-8") as f:
            steps :list[dict] = yaml.safe_load(f)
            for step in steps:
                if 'by' in step.keys():
                    element = self.find(step['by'],step['locator'])
                if 'action' in step.keys():
                    if 'click' == step['action']:
                        element.click()
                    if 'send' == step['action']:
                        #content = "{value}"
                        content:str = step['value']

                        for param in self._params:
                            """self._params["value"] = value"""
                            content = content.replace("{%s}"%param, self._params[param])
                        self.send(content, step['by'], step['locator'])
