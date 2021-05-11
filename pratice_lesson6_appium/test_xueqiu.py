# -*- coding:utf-8 -*-
__author__ = 'Tnew'
"""
app信息：
获取当前界面元素：adb shell dumpsys activity top(推荐)
获取任务列表: adb shell dumpsys activity activities

app入口:
adb logcat |grep -i displayed(推荐)
如果是windows系统，1 adb shell 2 logcat |grep -i displayed

启动应用：
adb shell am start -W -n com.xueqiu.android/.view.WelcomeActivityAlias -S（重点）
"""
from appium import webdriver
class TestDemo:
    def setup(self):

        desire_cap ={
            "platformName":'android',
            "deviceName":'127.0.0.1:7555',
            "appPackage":'com.xueqiu.android',
            "appActivity":'.view.WelcomeActivityAlias',
            "udid":"127.0.0.1:7555",
            "noReset":False
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desire_cap)
        self.driver.implicitly_wait(10)
    def test_demo(self):
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        el1.click()
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el2.send_keys("alibaba")
        el3 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.TextView[1]")
        el3.click()