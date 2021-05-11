# -*- coding:utf-8 -*-
__author__ = 'Tnew'


"""
@allure.step():只能以装饰器的形式放在类或者方法上面
with allure.step():可以放在测试用例方法里面，但测试步骤的代码需要被该语句包含
"""
import time
import allure
import pytest
from selenium import webdriver

@allure.testcase("http://www.github.com")
@allure.feature("百度搜索")
@pytest.mark.parametrize('test_data',['allure','pytest','unittest'])
def test_steps_demo(test_data):
    with allure.step("打开百度网页"):
        driver = webdriver.Chrome('C:/Python37/chromedriver.exe')
        # driver = webdriver.Chrome()
        driver.get("https://www.baidu.com")
        driver.maximize_window()

    with allure.step("定位输入框，输入数据"):
        driver.find_element_by_id("kw").send_keys(test_data)
        time.sleep(2)
    with allure.step("点击"):
        driver.find_element_by_id("su").click()
        time.sleep(2)

    with allure.step("保存图片"):
        driver.save_screenshot('./result/b.png')
        allure.attach.file('./result/b.png',attachment_type=allure.attachment_type.PNG)
        allure.attach("<head></head><body>首页</body>",'Attach with HTML type',allure.attachment_type.HTML)
    with allure.step("退出浏览器"):
        driver.quit()