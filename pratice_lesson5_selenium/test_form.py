"""
操作表单元素步骤：
首先定位到表单元素
然后操作元素(清空，输入等)
https://testerhome.com/account/sign_in
"""
from time import sleep

from selenium import webdriver
class TestForm:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.find_element_by_id("user_login").send_keys("tnew_tao@163.com")
        self.driver.find_element_by_id("user_password").send_keys("Tfl_900126")
        # sleep(3)
        # self.driver.find_element_by_id("user_remember_me").click()
        #第一种可行
        ele = self.driver.find_element_by_id("user_remember_me")
        webdriver.ActionChains(self.driver).move_to_element(ele).click().perform()

        #第二种不可行
        # ele = self.driver.execute_script("return document.getElementById('user_remember_me')")
        # ele.click()

        #第三种可行
        # ele = self.driver.find_element_by_id("user_remember_me")
        # self.driver.execute_script("arguments[0].click()",ele)
        # sleep(4)

        self.driver.find_element_by_xpath("//*[@id='new_user']/div[4]/input").click()
        sleep(4)