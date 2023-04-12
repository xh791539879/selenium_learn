import time
from time import sleep
from webdriver_helper import get_webdriver
from pageobject.login_page import LoginPage

"""
测试登录
"""


class TestSsgw:
    def setup_method(self):
        self.driver = get_webdriver()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)  # 隐性等待

    def teardown_method(self):
        time.sleep(5)

    def test_login(self):
        lp = LoginPage(self.driver)
        lp.login_sgw("hnssgw", "123456")  # 调用封装好的方法,即可实现登录,传入账号密码
        sleep(5)
