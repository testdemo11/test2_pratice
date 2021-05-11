"""
多窗口切换：通过句柄，切换句柄，可以在多个页面操作

1 先获取当前的窗口句柄（driver.current_window_handle）
2 再获取到所有的窗口句柄（driver.window_handles）
3 判断是否是想要操作的窗口，是，就对窗口操作，不是就对另一个窗口进行操作（driver.switch_to_window）
"""
from time import sleep

from pratice_lesson5_selenium.base import Base


class TestWindows(Base):
    def test_window(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        # print(self.driver.current_window_handle)
        self.driver.find_element_by_link_text("立即注册").click()
        window = self.driver.window_handles
        self.driver.switch_to_window(window[-1])
        # print(self.driver.current_window_handle)
        # print(self.driver.window_handles)
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("username")
        self.driver.find_element_by_id('TANGRAM__PSP_4__phone').send_keys('13917540883')
        sleep(2)
        self.driver.switch_to_window(window[0])
        self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("username")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys('password')
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
