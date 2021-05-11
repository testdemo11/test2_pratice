# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

"""
toast是个系统级别的空间，属于系统settings
appium 使用uiautomator底层的机制抓取toast，并且把toast放到控件树里面，但本身不属于控件
automationName:uiautomator2
getPageSource是无法找到的
必须使用xpath查找
//*[@class='android.widget.Toast']
//*[contains(@text,'xxxx')]

通过以下命令查找当前进程
adb shell
dumpsys window|grep mCurrent


"""
class TestToast:
    def setup(self):
        desire_caps = {}
        desire_caps["platformName"] = 'android'
        desire_caps["deviceName"] = '127.0.0.1:7555'
        desire_caps["appPackage"] = 'io.appium.android.apis'
        desire_caps["appActivity"] = '.view.PopupMenu1'
        desire_caps["noReset"] = "true"
        # desire_caps['dontStopAppOnReset'] = 'true'
        desire_caps['skipDeviceInitialization'] = 'true'
        desire_caps['unicodeKeyBoard']='true'
        desire_caps['resetKeyBoard'] = 'true'
        desire_caps['automationName'] = 'uiautomator2'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
    def test_toast(self):
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID,'Make a Popup!').click()
        self.driver.find_element(MobileBy.XPATH,'//*[@text="Search"]').click()
        # print(self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text)
        print(self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"Clicked popup")]').text)
        # print(self.driver.page_source)