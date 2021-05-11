# -*- coding:utf-8 -*-
__author__ = 'Tnew'


from selenium.webdriver.common.by import By

from pratice_lesson5_selenium.po_wework.PO_add_contactor.page.add_member_page import AddMemberPage


from pratice_lesson5_selenium.po_wework.PO_add_contactor.page.basepage import BasePage

#企业微信的主页面
class MainPage(BasePage):
    base_url = 'https://work.weixin.qq.com/wework_admin/frame'

    def goto_add_member(self):
        """
        添加成员
        :return:
        """
        #click add member
        self.find(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(1)').click()
        #return AddMemberPage()
        return AddMemberPage(self.driver)