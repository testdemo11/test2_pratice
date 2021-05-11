# -*- coding:utf-8 -*-
__author__ = 'Tnew'

import allure


@allure.link("http://www.baidu.com",name="baidu")
def test_with_link():
    print("这是链接")

TEST_CASE_LINK = "https://github.com"
@allure.testcase(TEST_CASE_LINK,'登录用例')
def test_with_case_link():
    print("这是测试用例链接")

#--allure-link-pattern = issue:http://www.mytesttracker/issue/{}
# “”“通过这种方式执行pytest test_allurelink.py --allure-link-pattern=issue:http://www.mytesttracker/issue/{} --alluredir=./result/6
@allure.issue('140','这是issue')
def test_with_issue_link():
    pass