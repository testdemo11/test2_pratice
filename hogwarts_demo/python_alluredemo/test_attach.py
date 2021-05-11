# -*- coding:utf-8 -*-
__author__ = 'Tnew'

import allure


def test_attach_text():
    allure.attach("这是一个纯文本",attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
    allure.attach("<body>这是一个html的body</body>",'html测试块',attachment_type=allure.attachment_type.HTML)

def test_attach_photo():
    allure.attach.file("C:/Users/narak\PycharmProjects/test2/hogwarts_demo/python_alluredemo/resource/test.jpg",name='图片',
                  attachment_type=allure.attachment_type.JPG)