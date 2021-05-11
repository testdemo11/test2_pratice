# -*- coding:utf-8 -*-
__author__ = 'Tnew'

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

"""
adb shell
dumpsys window|grep mCurrent 得到activity

com.tencent.wework/com.tencent.wework.launch.WwMainActivity

chromedriver可以有三种方式放置
1 放在appium默认路径下面，对应版本就行'D:/Study/Automation_Tester_Guide/Lesson6_appium/Appium-windows-1.19.1/resources/app/node_modules/appium/node_modules/appium-chromedriver/chromedriver/win'
2 设置 "ChromedriverExecutable":"D:/Study/Automation_Tester_Guide/Lesson6_appium/chromedriver"
3 可以用mapping.json的方式匹配，新建json,对应版本号映射匹配，然后在caps里面设置
                "chromedriverExecutableDir":"D:/Study/Automation_Tester_Guide/Lesson6_appium/chromedriver"
                "chromedriverChromeMappingFile": mapping.json的对应绝对路径
"""
from appium import webdriver


class TestDW:
    def setup(self):
        desire_caps = {
            "platformName":'android',
            "deviceName":'192.168.216.101:5555',
            "appPackage":'com.xueqiu.android',
            "appActivity":'com.xueqiu.android.common.MainActivity',
            "noReset":'true',
            "ChromedriverExecutable":"D:/Study/Automation_Tester_Guide/Lesson6_appium/chromedriver"
        }
        # desire_caps['dontStopAppOnReset'] = 'true'
        # desire_caps['skipDeviceInitialization'] = 'true'
        # desire_caps['unicodeKeyBoard']='true'
        # desire_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_caps)
        self.driver.implicitly_wait(5)
        # desire_caps['ChromedriverExecutable']='D:/Study/Automation_Tester_Guide/Lesson6_appium/Appium-windows-1.19.1/resources/app/node_modules/appium/node_modules/appium-chromedriver/chromedriver/win'

    def teardown(self):
        self.driver.quit()

    def test_xueqiu(self):
        """
        打开雪球
        点击交易
        点击A股开户
        输入手机和验证码
        点击立即开户

        :return:
        """
        print(self.driver.contexts)
        #点击交易
        self.driver.find_element(MobileBy.XPATH,"//*[@text='交易']").click()
        print(self.driver.contexts)
        #切换上下文
        self.driver.switch_to.context(self.driver.contexts[-1])
        print(self.driver.window_handles)
        #点击A股开户
        a_locator = (MobileBy.XPATH,"//*[@id='app']/div/div/div/ul/li[1]/div[2]/h1")
        WebDriverWait(self.driver,20).until(expected_conditions.element_to_be_clickable(a_locator))
        self.driver.find_element(*a_locator).click()

        print(self.driver.window_handles)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        #输入用户名
        user_locator = (MobileBy.XPATH,"//*[@id='phone-number']")
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(user_locator))
        self.driver.find_element(*user_locator).send_keys("13918342345")
        #输入密码
        self.driver.find_element(MobileBy.ID,"code").send_keys("152452")
        self.driver.find_element(MobileBy.XPATH,'/html/body/div/div/div[2]/div/div[2]/h1').click()


