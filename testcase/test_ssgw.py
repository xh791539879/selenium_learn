"""
省少工委测试用例
"""

from time import sleep
import allure
import pytest

import base.base_page
from pageobject.login_page import LoginPage
from pageobject.lzkh_page import LzkhPage


@allure.feature('登录模块')
class TestSsgw:
    @pytest.mark.usefixtures("login_assert") #调用断言
    @allure.story('正例:登录成功')
    def test_login_success(self):  # 登录
        # 操作主体
        self.driver = base.base_page.driver
        lp = LoginPage()
        lp.login_sgw("hnssgw", "123456")  # 先登录

    @pytest.mark.usefixtures("login_assert")  # 调用断言
    @allure.story('反例:丢失用户名')
    def test_login_lostname(self):  # 登录
        # 操作主体
        self.driver = base.base_page.driver
        lp = LoginPage()
        lp.login_sgw("", "123456")  # 先登录

    @pytest.mark.usefixtures("login_assert")  # 调用断言
    @allure.story('反例:丢失密码')
    def test_login_lostpassword(self):  # 登录
        # 操作主体
        self.driver = base.base_page.driver
        lp = LoginPage()
        lp.login_sgw("hnssgw", "")  # 先登录

    @pytest.mark.usefixtures("login_assert")  # 调用断言
    @allure.story('反例:非本角色')
    def test_login_not(self):  # 登录
        # 操作主体
        self.driver = base.base_page.driver
        lp = LoginPage()
        lp.login_sgw("zzssgw", "123456")  # 先登录


    def test_lzkh(self):  # 发布考核
        lp = LoginPage()
        lp.login_sgw("hnssgw", "123456")  # 先登录
        sleep(5)
        et = LzkhPage()
        et.publish_lzkh()
