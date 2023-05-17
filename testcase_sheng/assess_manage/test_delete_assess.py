from time import sleep

import allure
import pytest
from selenium.common import NoSuchElementException, exceptions

from Util.error_screenshot_util import save_error_screenshot
from pageobject.pagesheng.page_assess import PageAssess

test_name_select_data = ["测试新增考核"]


class TestDeleteAssess:
    @pytest.mark.usefixtures('set_sheng')
    @allure.story('删除--测试用例')
    @pytest.mark.parametrize("name_select", test_name_select_data)  # 将数据传入测试用例
    def test_del_assess(self, name_select, log, driver):  # 获取driver对象，执行测试用例之前必须初始化driver
        """
        :param name_select:通过'考核名称'查询并删除
        :param log:日志
        :param driver:驱动
        :return:无
        """
        log.logger.info("测试用例：删除考核，开始")
        sleep(5)
        del_assess = PageAssess(driver)
        title_before, title_after = del_assess.del_table(0)
        print(title_before)
        print(title_after)
        try:
            assert title_after != title_before
            log.logger.info(f"测试自动化测试考核名称，名称为{title_before}考核删除成功")
        except AssertionError as e:
            msg = f"删除断言失败，名为{title_before}的考核还存在"
            log.logger.error(msg)
            print(f"异常原因：{msg}")  # 打印异常原因
            save_error_screenshot("删除考核断言失败截图", driver, 'delete_assess_image')
            raise e  # 抛出异常,否则用例会被判断为pass
        except (NoSuchElementException, exceptions.TimeoutException) as e:  # 如果是没找到元素
            msg = f"元素定位失败，具体错误信息{e}"
            log.logger.error(msg)
            print(f"异常原因：{msg}")  # 打印异常原因
            save_error_screenshot("查询元素定位失败截图", driver, 'delete_assess_image')
            pytest.fail(reason="元素定位失败")
        except Exception as e:
            msg = f"其他错误，具体错误信息{e}"
            log.logger.error(msg)
            print(f"异常原因：{msg}")
            save_error_screenshot("查询其他错误截图", driver, 'delete_assess_image')
            raise e
        finally:
            log.logger.info(f"测试用例结束，考核年度：{title_before}删除操作测试完成")
            allure.attach(driver.get_screenshot_as_png(), "用例执行结果截图",
                          attachment_type=allure.attachment_type.PNG)  # 将用例最终截图打印到allure报告，无论失败与否都打印
            allure.attach(f"删除的考核名称为：{title_before},实际查询到的结果为：{title_after}",
                          "用例执行结果描述")  # 将实际结果打印到allure报告
