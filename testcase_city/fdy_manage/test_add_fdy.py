import sys
from time import sleep

import allure
import pytest
from selenium.common import exceptions, NoSuchElementException
from selenium.webdriver.common.by import By

from Util.error_screenshot_util import save_error_screenshot
from pageobject.pagecity.page_add_fdy import PageFdy

sys.path.append('common')
from common.makeinfo import get_name, get_idnum

x = get_name()  # 调用common公共方法生成随机姓名

y = get_idnum()  # 调用common公共方法生成随机身份证

test_data = [(x, y)]  # 数据驱动


@allure.feature('新增辅导员模块')
class TestAddFdy:

    @allure.story('新增辅导员--测试用例')
    @pytest.mark.usefixtures('set_city')
    @pytest.mark.parametrize(('name', 'number'), test_data)
    def test_add_fdy(self, log, driver, name, number):
        """
        :param log:日志
        :param driver:驱动
        :param name:辅导员姓名
        :param number:辅导员身份证
        :return:无
        """

        log.logger.info("测试用例：新增辅导员，开始")
        pf = PageFdy(driver)
        pf.add_fdy(name, number)
        sleep(2)
        fdy_name, fdy_number, fdy_class, fdy_upper = '', '', '', ''
        try:
            fdy_name = driver.find_element(By.XPATH, "//tr[1]//td[2]").text
            fdy_number = driver.find_element(By.XPATH, "//tr[1]//td[3]").text
            fdy_class = driver.find_element(By.XPATH, "//tr[1]//td[4]").text
            fdy_upper = driver.find_element(By.XPATH, "//tr[1]//td[5]").text
            assert fdy_name == name
            assert fdy_number == number
            assert fdy_class == "地市总辅导员"
            assert fdy_upper == "郑州市少工委"
            log.logger.info(f"辅导员类型：地市总辅导员,辅导员名称{name}，辅导员身份证{number}：新增成功")
        except AssertionError as e:
            msg = f"辅导员类型：地市总辅导员,辅导员名称{name}，辅导员身份证{number}：新增断言失败，实际为{fdy_name}，{fdy_number}，{fdy_class}，{fdy_upper}"
            log.logger.error(msg)
            print(f"异常原因：{msg}")
            save_error_screenshot("新增辅导员断言失败截图", driver, 'add_fdy_images')
            raise e
        except (NoSuchElementException, exceptions.TimeoutException) as e:  # 如果是没找到元素
            msg = f"元素定位失败，具体错误信息{e}"
            log.logger.error(msg)
            print(f"异常原因：{msg}")  # 打印异常原因
            save_error_screenshot("登录元素定位失败截图", driver, 'add_fdy_images')
            pytest.fail(reason="元素定位失败")
        except Exception as e:
            msg = f"其他错误，具体错误信息{e}"
            log.logger.error(msg)
            print(f"异常原因：{msg}")
            save_error_screenshot("新增辅导员其他错误截图", driver, 'add_fdy_images')
            raise e
        finally:
            log.logger.info(f"测试用例执行结束：辅导员类型：地市总辅导员,辅导员名称{name}，辅导员身份证{number}")
            allure.attach(driver.get_screenshot_as_png(), "用例执行结果截图",
                          attachment_type=allure.attachment_type.PNG)
            allure.attach(f"辅导员类型：地市总辅导员,辅导员名称{name}，辅导员身份证{number}")
