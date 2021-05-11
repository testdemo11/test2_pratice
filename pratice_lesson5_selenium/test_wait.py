#直接等待
#time.sleep(2)
#隐式等待,轮询查找（default 0.5s）,全局等待
#self.driver.implicitly_wait(2)
#显式等待 WebDriverWait 配合until,until_not()，判断进行等待
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://home.testing-studio.com/")
        self.driver.implicitly_wait(3)
    def test_wait(self):
        self.driver.find_element(By.XPATH,"//*[@title='所有分类']").click()
        sleep(3)
        # self.driver.find_element(By.XPATH,"//*[@title='测试答疑']").click()
        # sleep(3)
        # def wait(x):
        #     return len(self.driver.find_elements(By.XPATH,"//*[@class='table-heading']")) > 1
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located((By.XPATH,"//*[@class='table-heading']")))
        # sleep(3)
        self.driver.find_element(By.XPATH, "//*[@title='招聘内推']").click()
        sleep(3)
        self.driver.quit()
