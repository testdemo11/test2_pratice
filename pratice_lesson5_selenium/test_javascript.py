"""
直接使用js操作页面，能解决很多click()不生效的问题
页面滚动到底部，顶部
处理富文本，时间控件的输入

window.alert("selenium弹框测试")
a = document.getElementById("kw").value
document.title
JSON.stringify(performance.timing)

selenium如何调用js,selenium提供了一个内置方法execute_script()
driver.execute_script("window.alert("selenium弹框测试")")
driver.execute_script("a = document.getElementById("kw").value;window.alert(a)")

返回：
driver.execute_script("return document.getElementById("kw").value")

"""
import time
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pratice_lesson5_selenium.base import Base


class TestJs(Base):
    def test_js_scroll(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element(By.XPATH, "//*[@id='kw']").send_keys("selenium测试")
        ele = self.driver.execute_script("return document.getElementById('su')")
        ele.click()
        self.driver.execute_script("document.documentElement.scrollTop=100000")
        sleep(5)
        self.driver.find_element_by_xpath("//*[@id='page']/div/a[10]").click()
        sleep(3)
        # for code in ['return document.title','return JSON.stringify(performance.timing)']:
        #     print(self.driver.execute_script(code))
        print(self.driver.execute_script("return document.title;return JSON.stringify(performance.timing)"))

    def test_timereadonly(self):
        self.driver.get("https://www.12306.cn/index/")
        # time_element = self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').removeAttribute('readonly')")
        time.sleep(3)
        self.driver.execute_script("document.getElementById('train_date').value='2021-02-06'")
        # time.sleep(3)
        # self.driver.find_element_by_id("train_date").send_keys(Keys.CLEAR)
        # self.driver.find_element_by_id("train_date").send_keys("2021-2-6")
        # print(self.driver.find_element_by_id("train_date").text)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
        # time.sleep(5)

