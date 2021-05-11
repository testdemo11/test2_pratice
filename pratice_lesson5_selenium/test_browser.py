import os
from time import sleep

from selenium import webdriver

from pratice_lesson5_selenium.base import Base


class TestFrame:
    def setup(self):
        browser = os.getenv("browser")
        print(browser)
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            option = webdriver.ChromeOptions()
            option.add_experimental_option('w3c',False)
            self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
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