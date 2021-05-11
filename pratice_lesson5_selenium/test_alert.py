"""
alert操作：
switch_to.alert()：获取当前页面的警告框
text:获取提示信息
accept():接受现有警告框
dismiss():解散现有警告框
send_keys(keysToSend)：发送文本至警告框；keysToSend:将文本发送至警告框
"""
from time import sleep

from selenium import webdriver

from pratice_lesson5_selenium.base import Base


class TestAlert(Base):
    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        drag = self.driver.find_element_by_id("draggable")
        drop = self.driver.find_element_by_id("droppable")
        webdriver.ActionChains(self.driver).drag_and_drop(drag,drop).perform()
        sleep(3)
        #点击alert确认
        self.driver.switch_to.alert.accept()

        self.driver.switch_to.default_content()
        self.driver.find_element_by_id("submitBTN")
        sleep(5)