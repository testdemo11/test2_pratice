"""
find_element by id,name,xpath,css selector
xpath从头到尾遍历，速度慢，appium,selenium都可以用

xpath:
/bookstore/book[1]: bookstore子元素的第一个book元素
/bookstore/book[last()]: bookstore子元素的最后一个book元素
/bookstore/book[last()-1]: bookstore子元素的倒数第二个book元素
//title[@lang='eng']:选取所有title元素
/bookstore//book： bookstore下面的所有book子孙元素

css selector:
appium 只能用于手机中的网页
selenium
# id
. class
div,p:所有div和所有p的元素
div p :div下面的子孙元素 相当于xpath //
div>p :div下面的子元素 相当于xpath /
p:nth-child(2)  选择其父元素的第二个元素的每个p元素
'#s_tab a:nth-child(2)' s_tab 下面所有的a， a的父元素的第二个孩子
'#s_tab a:nth-last-child(1)' s_tab 下面所有的a,a的父元素的最后一个孩子
"""
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLocate:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")
    def test_locate(self):
        self.driver.find_element(By.XPATH,"//*[@id='kw']").send_keys("selenium")
