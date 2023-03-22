from selenium.webdriver.common.by import By

from base.base_page import BasePage


class LoginPage(BasePage):

    # 将页面中会用到的元素统一封装在这里
    current_url = "http://192.168.0.40:18400/index#/login"  #url
    username_loc = (By.ID, "name")    #用户名输入框
    password_loc = (By.ID, "password")  #密码
    login_sub = (By.XPATH, "//button[@class='ant-btn ant-btn-primary login-btn ant-btn-lg']")  #登录按钮

    # 将页面中会用到的动作统一封装在这里
    def login_sgw(self):
        self.open_browser()
        self.get(self.current_url)
        self.send_keys(self.username_loc,"hnssgw")
        self.send_keys(self.password_loc,"123456")
        self.click(self.login_sub)