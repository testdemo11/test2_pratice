# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from appium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

"""
74.0.3729.186
微信小程序自动化代码：
模拟器：Genymotion
系统版本：8.1
微信版本：7.0.15
小程序：雪球
https://ceshiren.com/t/topic/9969


https://github.com/m9rco/Genymotion_ARM_Translation :针对android不同版本的Genymotion-ARM-Translation
http://www.360doc.com/content/20/0331/18/21412_903018845.shtml： gitee账号 13917540883 Tfl_900126
解决apk安装到genymotion报错：https://ceshiren.com/t/topic/4058（模拟器是x86架构，手机是arm架构，把模拟器刷成arm）
如果遇见刷不成功的（提示copied成功就是没成功，成功是提示重启手机）
                1 genymotion setting adb设置成custom Android SDK tools,
                2 adb push D:\\android_studio_tools\Genymotion-ARM-Translation.zip /sdcard/Download/
                3 adb shell flash-archive.sh /sdcard/download/Genymotion-ARM-Translation.zip




测试人社区 https://ceshiren.com
mitmdump -p 5038 --rawtcp --mode reverse:http://localhost:5037/ -s adb.py

如何小程序自动化(设置chromedriver正确版本)
1 pip install mitmproxy（windows）
2 mitmdump -p 5038 --rawtcp --mode reverse:http://localhost:5037/ -s adb_proxy.py
3 基本capability设置
    appActivity:'com.tencent.mm.ui.LauncherUI'
    adbPort:5038
4 设置chromedriver正确版本
5 chrome option 传递给chromedriver

com.tencent.mm/com.tencent.mm.ui.LauncherUI
"""

class TestWxMicro:
    def setup(self):
        desire_caps = {
            "platformName": 'android',
            "deviceName": '192.168.216.103:5555',
            "appPackage": 'com.tencent.mm',
            "appActivity": 'com.tencent.mm.ui.LauncherUI',
            "noReset": 'true',
            'unicodeKeyBoard': 'true',
            'resetKeyBoard': 'true',
            "ChromedriverExecutable": "D:/Study/Automation_Tester_Guide/Lesson6_appium/chromedriver",
            "chromeOptions": {'androidProcess': 'com.tencent.mm:appbrand0'},
            "adbPort": 5038
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(30)

        self.driver.find_element(By.XPATH,"//*[@text='Contacts']")
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass

    def test_search(self):
        #原生自动化测试
        size = self.driver.get_window_size()
        width = size.get("width")
        height = size.get("height")
        self.driver.swipe(int(width*0.5),int(height*0.2),int(width*0.5),int(height*0.9),2000)
        self.driver.find_element(By.ID,"com.tencent.mm:id/dt5").click()
    #     # self.driver.find_element(By.CLASS_NAME,'android.widget.EditText').click()
    #     # self.driver.find_element(By.XPATH,"//*[@text='取消']")
    #     # self.driver.find_element(By.CLASS_NAME, 'android.widget.EditText').send_keys("雪球")
    #     # self.driver.find_element(By.CLASS_NAME, 'android.widget.Button')
    #     # self.driver.find_element(By.CLASS_NAME, 'android.widget.Button').click()
    #     # self.driver.find_element(By.XPATH, "//*[@text='自选']")
    #
        print(self.driver.contexts)
    #
    #     #进入webview
        self.driver.switch_to.context("WEBVIEW_xweb")
        self.driver.implicitly_wait(10)
        self.find_top_window()
    #
    #
    #     #css定位/html/body/wx-scroll-view/div/div[1]/div/wx-view/wx-view[3]/wx-navigator/wx-image/div
    #     self.driver.find_element(By.CSS_SELECTOR,"body > wx-scroll-view > div > div.wx-scroll-view > div > wx-view > wx-view._div.data-v-5667385e.optional__list-none > wx-navigator > wx-image > div").click()
    #     # self.driver.find_element(By.CSS_SELECTOR,"[src*=stock_add]").click()
    #     #等待新窗口
    #     WebDriverWait(self.driver,30).until(lambda x: len(self.driver.window_handles) > 2)
    #     self.find_top_window()
    #     self.driver.find_element(By.XPATH,"/html/body/wx-view/wx-view[1]/wx-view/wx-input/div[1]/div[1]").click()
    #     # # self.driver.find_element(By.CSS_SELECTOR, "._input").click()
    #     # #输入
    #     # self.driver.switch_to.context("NATIVE_APP")
    #     # ActionChains(self.driver).send_keys("alibaba").perform()
    #     #
    #     # #点击
    #     # self.driver.switch_to.context("WEBVIEW_xweb")
    #     # self.driver.find_element(By.CSS_SELECTOR, ".stock_item")
    #     # self.driver.find_element(By.CSS_SELECTOR, ".stock_item").click()
    #
    def find_top_window(self,driver=None):
        for window in self.driver.window_handles:
            print(window)
            if ":VISIBLE" in self.driver.title:
                print("find")
                print(self.driver.title)
            else:
                self.driver.switch_to.window(window)

    # def test_search1(self):
    #     self.driver.find_element_by_xpath("//*[@text='Contacts']")
    #     size = self.driver.get_window_size()
    #     width = size.get("width")
    #     height = size.get("height")
    #     self.driver.swipe((width / 2), int((height * 0.2)), (width / 2), (height * 0.8), 2000)
    #     self.driver.find_element_by_xpath("//*[@resource-id='com.tencent.mm:id/dt5']").click()
    #     print(self.driver.contexts, '第一次打印')
    #     self.driver.find_element_by_xpath("//*[@content-desc='搜索股票信息/代码']/..").click()



