import allure
import pytest
from selenium.common import exceptions, NoSuchElementException
from selenium.webdriver.common.by import By

from Util.error_screenshot_util import save_error_screenshot
from pageobject.pagecity.page_add_fdy import PageFdy

test_name_data = ['郑州二中队']


@allure.feature('查询辅导员模块')
class TestSearchFdy:
    @allure.story('按姓名查询辅导员--测试用例')
    @pytest.mark.usefixtures('set_city')
    @pytest.mark.parametrize('name', test_name_data)
    def test_search_by_name(self, log, driver, name):
        log.logger.info("测试用例：按姓名查询辅导员，开始")
        pf = PageFdy(driver)
        pf.search_by_name(name)
        try:
            fdy_name = driver.find_element(By.XPATH, "//tr[1]//td[2]").text
            assert fdy_name == name
            log.logger.info(f"通过姓名查询辅导员：{name}：查询成功，用例通过")
        except AssertionError as e:
            msg = f"通过姓名查询辅导员：{name}：查询失败，断言失败"
            log.logger.error(msg)
            save_error_screenshot("查询辅导员断言失败截图", driver, 'search_fdy_images')
            raise e
        except (NoSuchElementException, exceptions.TimeoutException) as e:  # 如果是没找到元素
            msg = f"元素定位失败，具体错误信息{e}"
            log.logger.error(msg)
            print(f"异常原因：{msg}")  # 打印异常原因
            save_error_screenshot("登录元素定位失败截图", driver, 'search_fdy_images')
            pytest.fail(reason="元素定位失败")
        except Exception as e:
            msg = f"其他错误，具体错误信息{e}"
            log.logger.error(msg)
            print(f"异常原因：{msg}")
            save_error_screenshot("查询辅导员其他错误截图", driver, 'search_fdy_images')
            raise e
        finally:
            log.logger.info(f"测试用例执行结束；按姓名查询辅导员：{name}：查询完成")
            allure.attach(driver.get_screenshot_as_png(), "用例执行结果截图",
                          attachment_type=allure.attachment_type.PNG)
            allure.attach(f"测试用例执行结束；按姓名查询辅导员：{name}：查询完成")
