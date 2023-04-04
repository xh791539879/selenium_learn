"""
省少工委测试用例
"""
import time
from time import sleep
from pageobject.login_page import LoginPage
from pageobject.lzkh_page import LzkhPage
from selenium.webdriver.support import expected_conditions as EC


class TestSsgw:

    def test_login(self):  # 登录
        lp = LoginPage()
        lp.login_sgw("hnssgw", "123456")  # 先登录


        # try:
        #     # 错误代码， 故意失败
        #     locator = (By.CLASS_NAME, "name1",)
        #     result = EC.presence_of_element_located(locator)
        #     print(result(self.driver))
        # except Exception as e:
        #     # 如果操作步骤过程中有异常，那么用例失败，在这里完成截图操作
        #     file_path = './error_image/登录失败截图.png'
        #     self.driver.save_screenshot(file_path)
        #     # 将截图展示在allure测试报告上
        #     with open(file_path,mode="rb") as f:
        #         allure.attach(f.read(),"登录失败截图.png",allure.attachment_type.PNG)

    def test_lzkh(self):  # 发布考核
        lp = LoginPage()
        lp.login_sgw("hnssgw", "123456")  # 先登录
        sleep(5)
        et = LzkhPage()
        et.publish_lzkh()
