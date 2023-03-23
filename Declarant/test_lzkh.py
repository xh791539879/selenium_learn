import time
import unittest
from time import sleep

from webdriver_helper import get_webdriver

from pageobject.login_page import LoginPage
from pageobject.lzkh_page import LzkhPage


class TestLzkh(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = get_webdriver()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)  # 隐性等待

    def tearDown(self) -> None:
        time.sleep(5)
    def testlzkh(self):
        lp = LoginPage(self.driver)
        lp.login_sgw("hnssgw", "123456")  # 先登录
        sleep(5)

        et = LzkhPage(self.driver)
        et.edit_lzkh()
