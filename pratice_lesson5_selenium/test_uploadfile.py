"""
通过send_keys来上传
"""
from pratice_lesson5_selenium.base import Base
from time import sleep

class TestUploadFile(Base):
    def test_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]").click()
        self.driver.find_element_by_id("uploadImg").send_keys("C:/Users/Local_Admin/PycharmProjects/tnewtest/pratice_lesson5_selenium/photo/1.png")
        sleep(3)