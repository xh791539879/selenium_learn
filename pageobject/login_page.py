from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    """
    页面类：登录页面

    current_url (str): 登录页面 URL 地址
    username_loc (tuple): 用户名输入框元素定位信息
    password_loc (tuple): 密码输入框元素定位信息
    login_sub (tuple): 登录按钮元素定位信息
    name_display_loc (tuple): 登录成功后角色名称显示元素定位信息

    """

    current_url = "http://192.168.0.40:18400/index#/login"  # url
    username_loc = (By.ID, "name")  # 用户名输入框
    password_loc = (By.ID, "password")  # 密码
    login_sub = (By.XPATH, "//button[@class='ant-btn ant-btn-primary login-btn ant-btn-lg']")  # 登录按钮
    name_display_loc = (By.CLASS_NAME, "name")

    def login_platform(self, username, password):
        """
        登录系统
        :param username: 用户名
        :param password: 密码
        :return: 登录后的角色名称
        """
        self.get(self.current_url)  # 打开登录页面
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_sub))  # 等待登录按钮可被点击
        self.send_keys(self.username_loc, username)  # 输入用户名
        self.send_keys(self.password_loc, password)  # 输入密码
        self.click(self.login_sub)  # 点击登录按钮
        sleep(5)  # 等待5s，手动验证滑块
        return self.get_text(self.name_display_loc)  # 返回登录后的角色名称显示文本
