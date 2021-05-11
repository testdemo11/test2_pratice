from selenium import webdriver

from pratice_lesson5_selenium.base import Base
from time import sleep


class TestDemo(Base):
    def test_demo(self):
        self.driver.get("https://testerhome.com")
        # self.driver.find_element_by_xpath("//*[@id='main-nav-menu']/li[1]/a").click()
        self.driver.find_element_by_link_text("社区").click()
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='main']/div/div[2]/div[1]/div/a").click()
        sleep(2)