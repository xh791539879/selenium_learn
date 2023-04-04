"""
省少工委测试用例
"""
import time
from time import sleep

import allure
from selenium.webdriver.common.by import By

import base.base_page
from pageobject.login_page import LoginPage
from pageobject.lzkh_page import LzkhPage
from selenium.webdriver.support import expected_conditions as EC


class TestSsgw:

    def test_login(self):  # 登录
        # 操作主体
        self.driver = base.base_page.driver
        lp = LoginPage()
        lp.login_sgw("hnssgw", "123456")  # 先登录
        # 断言主体
        text = self.driver.find_element(By.CLASS_NAME, "name").text
        try:
            assert text == "hhhh"
        except Exception as msg:
            print(u"异常原因%s" % msg)  # 打印异常原因
            # 如果操作步骤过程中有异常，那么用例失败，在这里完成截图操作
            file_path = './error_image/登录失败截图.png'
            self.driver.save_screenshot(file_path)
            # 将截图展示在allure测试报告上
            with open(file_path, mode="rb") as f:
                allure.attach(f.read(), "登录失败截图.png", allure.attachment_type.PNG)
            raise  # 抛出异常,否则用例会被判断为pass

    def test_lzkh(self):  # 发布考核
        lp = LoginPage()
        lp.login_sgw("hnssgw", "123456")  # 先登录
        sleep(5)
        et = LzkhPage()
        et.publish_lzkh()
