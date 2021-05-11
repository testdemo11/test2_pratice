# -*- coding:utf-8 -*-
__author__ = 'Tnew'

import allure
from selenium.webdriver.common.by import By

from pratice_lesson5_selenium.po_wework.PO_add_contactor.page.basepage import BasePage


class AddMemberPage(BasePage):
    def add_member(self,username,account,phonenum):
        """
        添加联系人，详细信息
        :return:
        """

        #输入用户名
        self.find(By.ID,'username').send_keys(username)
        #输入账号
        self.find(By.ID,'memberAdd_acctid').send_keys(account)
        #输入手机号
        self.find(By.ID,'memberAdd_phone').send_keys(phonenum)
        #点击保存，页面上有多个相同属性的元素，通过find_element找到的是第一个元素
        self.find(By.CSS_SELECTOR,'.js_btn_save').click()
        return True

    def get_member(self):
        """
        获取所有联系人姓名
        """
        #等待通讯录保存成功后的页面加载成功
        self.wait((By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)'))
        # 找到所有姓名对应的元素，通过找到class name为member_colRight_memberTable_td的父元素的第二个子元素来找到姓名
        eles_list = self.finds(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')
        names = []
        for ele in eles_list:
            names.append(ele.get_attribute('title'))
        return names



