"""
省少工委登录测试用例
"""
import time
import allure
import pytest
from selenium.common import exceptions
from selenium.webdriver.common.by import By
import base.base_page
from pageobject.login_page import LoginPage


driver = base.base_page.driver

test_login_data = [("hnssgw", "123456"), ("", "123456"), ("hnssgw", ""), ("zzssgw", "123456"),
                   ("123456", "123456")]  # 数据驱动，一组数据即为一条用例


@allure.feature('登录模块')  # 功能模块\场景
class TestLogin:
    @allure.step('测试登录')  # 测试用例的步骤
    @allure.severity('blocker')  # 测试用例的严重级别
    @allure.story('登录测试用例')  # 测试场景
    @allure.tag('smoke')  # 测试类型
    @pytest.mark.parametrize("username,password", test_login_data)  # 将数据传入测试用例
    def test_login(self, username, password, log):  # 登录
        """
        测试用例描述信息：验证登录功能是否正常
        :param username: 用户名
        :param password: 密码
        :param log: 日志对象
        """
        text = ''
        lp = LoginPage()
        lp.login_platform(username, password)  # 传入参数
        try:
            target = driver.find_element(By.CLASS_NAME, "name")
            try:
                text = target.text
                assert text == "河南省少工委"
                log.logger.info("用户名：{0}，密码：{1}，登录成功".format(username, password))
            except AssertionError as e:
                msg = "用户名：{0}，密码：{1}断言失败，实际登录角色为:{2}".format(username, password, text)
                log.logger.error(msg)
                now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
                print(u"异常原因%s" % msg)  # 打印异常原因
                imgname = now + "异常截图.png"
                # 如果操作步骤过程中有异常，那么用例失败，在这里完成截图操作
                file_path = 'error_image/login_image/' + imgname
                driver.save_screenshot(file_path)
                # 将截图展示在allure测试报告上
                with open(file_path, mode="rb") as f:
                    allure.attach(f.read(), imgname, allure.attachment_type.PNG)
                raise e  # 抛出异常,否则用例会被判断为pass
        except exceptions.NoSuchElementException as e:
            now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            print(u"异常原因%s" % e)  # 打印异常原因
            imgname = now + "异常截图.png"
            # 如果操作步骤过程中有异常，那么用例失败，在这里完成截图操作
            file_path = 'error_image/login_image/' + imgname
            driver.save_screenshot(file_path)
            # 将截图展示在allure测试报告上
            with open(file_path, mode="rb") as f:
                allure.attach(f.read(), imgname, allure.attachment_type.PNG)
            pytest.fail(msg="元素定位失败")
        finally:
            log.logger.info("用户名:{0}，密码:{1},登录验证完成".format(username, password))
            # 添加用例执行结果的附加信息到allure测试报告中
            allure.attach(driver.get_screenshot_as_png(), "用例执行结果截图",
                          attachment_type=allure.attachment_type.PNG)
            allure.attach("用户名：{0}，密码：{1}，实际登录角色为:{2}".format(username, password, text), "用例执行结果描述")




