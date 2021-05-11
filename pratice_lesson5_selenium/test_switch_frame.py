"""
frame :一种是嵌套，一种是未嵌套

切换frame
driver.switch_to.frame(): 根据元素id或者index切换frame
driver.switch_to.default_content(): 切换到默认frame
driver.switch_to.parent_frame(): 切换到父级frame

未嵌套frame
driver.switch_to.frame(“id"): 根据元素id或者index切换frame
driver.switch_to.frame(“index"):frame无id的时候根据索引来处理，索引从0开始driver.switch_to_frame(0)

嵌套frame
driver.switch_to.frame("父节点")
driver.switch_to.frame("子节点")
"""
from time import sleep

from selenium import webdriver

from pratice_lesson5_selenium.base import Base


class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        # drag = self.driver.find_element_by_id("draggable")
        # drop = self.driver.find_element_by_id("droppable")
        # webdriver.ActionChains(self.driver).drag_and_drop(drag,drop).perform()
        print(self.driver.find_element_by_id("draggable").text)
        sleep(3)
        # self.driver.switch_to.parent_frame()
        self.driver.switch_to.default_content()
        print(self.driver.find_element_by_id("submitBTN").text)