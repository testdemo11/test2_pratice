import os

from selenium import webdriver
"""
操作多浏览器
windows 下面需要命令行设置set browser=firefox,然后再当前设置窗口命令行运行pytest xxx.py,窗口关闭设置无效
ios系统,直接运行browser=firefox pytest xxx.py
"""

class Base:
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
