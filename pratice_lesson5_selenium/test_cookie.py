"""
#复用浏览器拿到登录信息的cookie
1 关闭所有chrome浏览器，然后把chrome.exe的路径放入环境变量中，chrome.exe路径可在chrome快捷图标右击属性得到
2 打开cmd,输入chrome --remote-debugging-port=9222
3 在新弹出的浏览器中输入你想复用的网页，带有登录的之类，然后可以输入localhost:9222看到你想复用的网页
4 此时代表你的设置已经完成，然后在你的代码中添加如下设置
        # option = Options()
        # option.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=option)
添加好后，就可以复用网页了，不用在代码里get网址 self.driver.get("https://work.weixin.qq.com/wework_admin/frame")，
只需要把你要复用的网页放在浏览器的最前面，然后就可以拿到cookies了 cookies = self.driver.get_cookies()

#
如果cookies里面有expiry 数据可能是浮点数，需要把这个信息去掉，防止报错
    for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie) add_cookie只能是字典，而拿到的cookies是列表，所以要遍历

#shelve python 提供的内置模块，相当于小型数据库
先要把cookies放到shelve中：如下
cookies = [{},{}]
db = shelve.open("./my_db/cookies") #创建一个package放数据,my_db创建好的文件夹（带有__init__.py），cookies不用创建
    db['cookie'] = cookies
    db.close() 运行一下

从shelve中拿数据
shelve.open("./my_db/cookies")
cookies= db['cookie']
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.refresh()

https://work.weixin.qq.com/wework_admin/frame
"""
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestCookie:
    def setup(self):
        # option = Options()
        # option.debugger_address = '127.0.0.1:9224'
        # self.driver = webdriver.Chrome(options=option)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()

    def test_cookie(self):
        #获取当前页面的cookie
        cookies = self.driver.get_cookies()
        print(cookies)

        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        #带有登录信息的cookie
        # cookies=[{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688853871869717'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'E2A_-D1HoBHV7HLGueur1MfSnjehwO_QU2jOFmZXfuqI4lNArS70pgBloSpSBS5r0s0vieW3QawnwVNUjxP2LHeFy0iUXOf5vGL_VIfqVm8pB0vOuRxTzpYV1iOaZRw6azuZ9W-qeNwVQpwX9z5_BGDMKboCNupnFrZmwkoH1_Mj1lm7-BzKaNY-Mw6_IqkIATTbQiVau43jPa-YNXuXHmRDQ_-nZz_9ZyqcnR0Ndc5x2budZWgyHrqAWYEUL2f1TJk5lF0BP1IwHnD-B1QhzQ'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688853871869717'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324981359321'}, {'domain': '.work.weixin.qq.com', 'expiry': 1644212716, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1612675843,1612676717'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a6805857'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1612676717'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '38485810622708259'}, {'domain': 'work.weixin.qq.com', 'expiry': 1612707358, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '8rosb41'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'Qj6iGALP_aA7sjXdV5MfmI5CNOc98IdSKVn4Bx8KdS28rAoJVtIopvT2xAuCJNCR'}, {'domain': '.work.weixin.qq.com', 'expiry': 1644211822, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1615269034.87, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'en'}]
        # for cookie in cookies:
        #     if 'expiry' in cookie.keys():
        #         cookie.pop("expiry")
        #     self.driver.add_cookie(cookie)
        # sleep(3)
        # self.driver.refresh()
        # sleep(3)

    def test_importcontact(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        #带有登录信息的cookie
        cookies=[{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688853871869717'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'E2A_-D1HoBHV7HLGueur1MfSnjehwO_QU2jOFmZXfuqI4lNArS70pgBloSpSBS5r0s0vieW3QawnwVNUjxP2LHeFy0iUXOf5vGL_VIfqVm8pB0vOuRxTzpYV1iOaZRw6azuZ9W-qeNwVQpwX9z5_BGDMKboCNupnFrZmwkoH1_Mj1lm7-BzKaNY-Mw6_IqkIATTbQiVau43jPa-YNXuXHmRDQ_-nZz_9ZyqcnR0Ndc5x2budZWgyHrqAWYEUL2f1TJk5lF0BP1IwHnD-B1QhzQ'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688853871869717'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324981359321'}, {'domain': '.work.weixin.qq.com', 'expiry': 1644212716, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1612675843,1612676717'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a6805857'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1612676717'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '38485810622708259'}, {'domain': 'work.weixin.qq.com', 'expiry': 1612707358, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '8rosb41'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'Qj6iGALP_aA7sjXdV5MfmI5CNOc98IdSKVn4Bx8KdS28rAoJVtIopvT2xAuCJNCR'}, {'domain': '.work.weixin.qq.com', 'expiry': 1644211822, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1615269034.87, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'en'}]
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        sleep(3)
        self.driver.find_element_by_xpath("//*[@id='_hmt_click']/div[1]/div[4]/div[2]/a[2]/div/span[2]").click()
        self.driver.find_element_by_id("js_upload_file_input").send_keys("C:/Users/Local_Admin/PycharmProjects/tnewtest/pratice_lesson5_selenium/excel/myname.xlsx")
        assert 'myname.xlsx' == self.driver.find_element_by_id("upload_file_name").text

    def test_shelve(self):
        #shelve python 提供的内置模块，相当于小型数据库
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 带有登录信息的cookie
        # cookies = [
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
        #      'value': '1688853871869717'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
        #      'value': 'E2A_-D1HoBHV7HLGueur1MfSnjehwO_QU2jOFmZXfuqI4lNArS70pgBloSpSBS5r0s0vieW3QawnwVNUjxP2LHeFy0iUXOf5vGL_VIfqVm8pB0vOuRxTzpYV1iOaZRw6azuZ9W-qeNwVQpwX9z5_BGDMKboCNupnFrZmwkoH1_Mj1lm7-BzKaNY-Mw6_IqkIATTbQiVau43jPa-YNXuXHmRDQ_-nZz_9ZyqcnR0Ndc5x2budZWgyHrqAWYEUL2f1TJk5lF0BP1IwHnD-B1QhzQ'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
        #      'value': '1688853871869717'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
        #      'value': '1970324981359321'}, {'domain': '.work.weixin.qq.com', 'expiry': 1644212716, 'httpOnly': False,
        #                                     'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/',
        #                                     'secure': False, 'value': '1612675843,1612676717'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
        #      'value': 'direct'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
        #      'value': '1'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
        #      'value': 'a6805857'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
        #      'path': '/', 'secure': False, 'value': '1612676717'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
        #      'value': '38485810622708259'},
        #     {'domain': 'work.weixin.qq.com', 'expiry': 1612707358, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
        #      'secure': False, 'value': '8rosb41'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
        #      'value': 'Qj6iGALP_aA7sjXdV5MfmI5CNOc98IdSKVn4Bx8KdS28rAoJVtIopvT2xAuCJNCR'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1644211822, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
        #      'path': '/', 'secure': False, 'value': '0'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1615269034.87, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
        #      'path': '/', 'secure': False, 'value': 'en'}]

        db = shelve.open("./my_db/cookies")
        # db['cookie'] = cookies
        # db.close()
        cookies= db['cookie']
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.refresh()
        sleep(3)
        self.driver.find_element_by_css_selector(".index_service_cnt_itemWrap:nth-child(2)").click()
        sleep(3)
        self.driver.find_element_by_id("js_upload_file_input").send_keys(
            "C:/Users/narak/PycharmProjects/test2/pratice_demo/pratice_cookie_weixin/excel/myname.xlsx")
        assert 'myname.xlsx' == self.driver.find_element_by_id("upload_file_name").text


