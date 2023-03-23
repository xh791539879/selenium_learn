import time
import unittest
from time import sleep
import pytest as pytest
from webdriver_helper import get_webdriver
from pageobject.login_page import LoginPage

"""
测试登录
"""


class TestInfor(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = get_webdriver()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)  # 隐性等待

    def tearDown(self) -> None:
        time.sleep(5)

    def test_login(self):
        lp = LoginPage(self.driver)
        lp.login_sgw("hnssgw", "123456")  # 调用封装好的方法,即可实现登录,传入账号密码
        sleep(5)
