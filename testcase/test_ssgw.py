"""
省少工委测试用例
"""
import time
from time import sleep
from selenium.webdriver.common.by import By
from webdriver_helper import get_webdriver
from pageobject.login_page import LoginPage
from pageobject.lzkh_page import LzkhPage
from selenium.webdriver.support import expected_conditions as EC

class TestSsgw:
    def setup_class(self):
        self.driver = get_webdriver()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)  # 隐性等待

    def setup_method(self):
        pass

    def teardown_method(self):
        time.sleep(5)

    def test_login(self): # 登录
        lp = LoginPage(self.driver)
        lp.login_sgw("hnssgw", "123456")  # 先登录
        locator = (By.CLASS_NAME, "name",)
        result = EC.presence_of_element_located(locator)
        print(result(self.driver))

    def test_lzkh(self):   #发布考核
        lp = LoginPage(self.driver)
        lp.login_sgw("hnssgw", "123456")  # 先登录
        sleep(5)
        et = LzkhPage(self.driver)
        et.publish_lzkh()
