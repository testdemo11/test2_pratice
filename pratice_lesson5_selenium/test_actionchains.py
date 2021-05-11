"""
action =ActionChains(driver)
action.方法1
action.方法2
action.方法3
action.perform()

ActionChains(driver).move_to_elment().perform()
"http://sahitest.com/demo/clicks.htm"
"http://sahitest.com/demo/dragDropMooTools.htm"


模拟按键操作
action.send_keys()

http://sahitest.com/demo/label.htm
"""
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from pratice_lesson5_selenium.base import Base
from time import sleep

class TestActionChains(Base):
    # @pytest.mark.skip
    def test_actionchains(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        ele_click = self.driver.find_element_by_xpath("/html/body/form/input[3]")
        ele_double = self.driver.find_element_by_xpath("/html/body/form/input[2]")
        ele_right = self.driver.find_element_by_xpath("/html/body/form/input[4]")
        action = ActionChains(self.driver)
        action.click(ele_click)
        sleep(2)
        action.context_click(ele_right)
        sleep(2)
        action.double_click(ele_double)
        sleep(2)
        action.perform()
        sleep(5)

    # @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get("http://www.baidu.com")
        ele = self.driver.find_element_by_xpath("//*[@id='s-usersetting-top']")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        #移到设置后才有搜索设置这个属性，注意位置
        search = self.driver.find_element_by_link_text("搜索设置")
        sleep(2)
        action.click(search)
        action.perform()

    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        ele_drag = self.driver.find_element_by_id("dragger")
        ele_drop = self.driver.find_element_by_xpath("/html/body/div[2]")

        action = ActionChains(self.driver)
        # action.click_and_hold(ele_drag).release(ele_drop).perform()
        # action.drag_and_drop(ele_drag,ele_drop).perform()
        action.click_and_hold(ele_drag).move_to_element(ele_drop).release().perform()
        sleep(2)

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        username = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        username.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACKSPACE).perform()
        sleep(2)

