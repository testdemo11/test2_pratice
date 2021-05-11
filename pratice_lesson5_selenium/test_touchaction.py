from selenium.webdriver import TouchActions

from pratice_lesson5_selenium.base import Base
from time import sleep

class TestTouchAction(Base):
    def test_touchaction(self):
        self.driver.get("http://www.baidu.com")
        el = self.driver.find_element_by_id("kw")
        search = self.driver.find_element_by_id('su')
        el.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(search)
        action.perform()

        action.scroll_from_element(el,0,10000).perform()
        sleep(3)