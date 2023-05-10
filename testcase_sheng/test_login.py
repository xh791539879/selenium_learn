"""
省少工委登录测试用例
"""
import time
import allure
import pytest
from selenium.common import exceptions, NoSuchElementException
from selenium.webdriver.common.by import By
import base.base_page
from Util.error_screenshot_util import save_error_screenshot
from pageobject.login_page import LoginPage

test_login_data = [("hnssgw", "123456"), ("", "123456"), ("hnssgw", ""), ("zzssgw", "123456"),
                   ("123456", "123456")]  # 数据驱动，一组数据即为一条用例


@allure.feature('登录模块')  # 功能模块\场景
class TestLogin:
    @allure.step('测试登录')  # 测试用例的步骤
    @allure.severity('blocker')  # 测试用例的严重级别
    @allure.story('登录测试用例')  # 测试场景
    @allure.tag('smoke')  # 测试类型
    @pytest.mark.parametrize("username,password", test_login_data)  # 将数据传入测试用例
    def test_login(self, username, password, log, driver):  # 登录
        """
        测试用例描述信息：验证登录功能是否正常
        :param username: 用户名
        :param password: 密码
        :param log: 日志对象
        """
        role = ''
        try:
            lp = LoginPage(driver)
            role = lp.login_platform(username, password)  # 传入参数
            assert role == "河南省少工委"
            log.logger.info(f"用户名：{username}，密码：{password}，登录成功，角色为:{role}")
        except AssertionError as e:
            msg = f"登录角色错误：用户名：{username}，密码：{password}，实际登录角色为:{role}"
            log.logger.error(msg)
            print(f"异常原因：{msg}")  # 打印异常原因
            save_error_screenshot("登录断言失败截图", driver, 'login_error')
            raise e  # 抛出异常,否则用例会被判断为pass
        except (NoSuchElementException, exceptions.TimeoutException) as e:  # 如果是没找到元素
            msg = f"元素定位失败，具体错误信息{e}"
            log.logger.error(msg)
            print(f"异常原因：{msg}")  # 打印异常原因
            save_error_screenshot("登录元素定位失败截图", driver, 'login_error')
            pytest.fail(reason="元素定位失败")
        except Exception as e:
            msg = f"其他错误，具体错误信息{e}"
            log.logger.error(msg)
            print(f"异常原因：{msg}")
            save_error_screenshot("登录其他错误截图", driver, 'login_error')
            raise e
        finally:
            log.logger.info(f"用户名:{username}，密码:{password},登录验证完成")
            # 添加用例执行结果的附加信息到allure测试报告中
            allure.attach(driver.get_screenshot_as_png(), "用例执行结果截图",
                          attachment_type=allure.attachment_type.PNG)  # 将用例最终截图打印到allure报告，无论失败与否都打印
            allure.attach(f"用户名：{username}，密码：{password}，实际登录角色为:{role}",
                          "用例执行结果描述")  # 将实际结果打印到allure报告
