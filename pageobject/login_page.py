"""
登录
"""
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage


class LoginPage(BasePage):
    # 将页面中会用到的元素统一封装在这里
    current_url = "http://192.168.0.40:18400/index#/login"  # url
    username_loc = (By.ID, "name")  # 用户名输入框
    password_loc = (By.ID, "password")  # 密码
    login_sub = (By.XPATH, "//button[@class='ant-btn ant-btn-primary login-btn ant-btn-lg']")  # 登录按钮

    # 将页面中会用到的动作统一封装在这里
    def login_platform(self, username, password):  # 用户名\密码不写死,在用例层调用
        self.get(self.current_url)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_sub))  # 等待元素可点击
        self.send_keys(self.username_loc, username)
        self.send_keys(self.password_loc, password)
        self.click(self.login_sub)
        sleep(5)  # 等待5s，手动验证滑块

