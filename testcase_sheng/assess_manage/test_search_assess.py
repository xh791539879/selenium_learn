from time import sleep

import allure
import pytest
from selenium.webdriver.common.by import By

from Util.error_screenshot_util import save_error_screenshot
from common.common import TableDataExtractor
from pageobject.pagesheng.page_assess import PageAssess

# 测试数据，仅包括考核名称
test_name_select_data = ["测试新增考核"]
# 测试数据，仅包括考核年度
test_year_select_data = ["2023"]


class TestSearchAssess:

    # 通过fixture来设置前置条件，即自动登录系统，并进入指定页面
    @pytest.mark.usefixtures('set_sheng')
    # 这是allure中的测试用例分类和标题
    @allure.story('按名称查询考核--测试用例')
    # parametrize装饰器将测试数据传入测试用例
    @pytest.mark.parametrize("name_select", test_name_select_data)
    def test_name_select_assess(self, name_select, log, driver):  # 获取driver对象，执行测试用例之前必须初始化driver
        """
        :param name_select:按照'考核名称'查询
        :param log:
        :param driver:
        :return:
        """

        # 记录日志
        log.logger.info("测试用例：按名称查询考核，开始")

        # 等待页面加载完成
        sleep(5)

        # 创建PageAssess对象，调用相应的方法进行测试操作
        select = PageAssess(driver)
        select.select_by_name(name_select)
        sleep(3)

        # 定位到查询结果表格，并通过TableDataExtractor获取表格中指定列的数据
        element = driver.find_element(By.CLASS_NAME, "ant-table-tbody")
        result_list = TableDataExtractor.get_column_data(element, 2)
        print(result_list)

        b = ""
        for b in result_list:
            print('列表数据遍历完成')

        try:
            # 对获取的数据进行断言比对，验证查询结果是否符合预期
            assert name_select in b, f"{b}不包含{name_select}"
            log.logger.info("考核名称{0}查询成功".format(name_select))
        except AssertionError as e:
            # 如果结果不符，则抛出异常，同时保存现场截图，用例会被判断为失败
            msg = f"查询的考核名称为：{name_select},实际查询到的结果为：{result_list}"
            log.logger.error(msg)
            print(f"异常原因：{msg}")
            save_error_screenshot("查询列表断言失败截图", driver, 'select_assess_image')
            raise e
        finally:
            # 记录日志，测试用例执行结束
            log.logger.info(f"测试用例结束，考核名称：{name_select}查询完成")
            allure.attach(driver.get_screenshot_as_png(), "用例执行结果截图",
                          attachment_type=allure.attachment_type.PNG)  # 将用例最终截图打印到allure报告，无论失败与否都打印
            allure.attach(f"查询的考核年度为：{name_select},实际查询到的结果为：{result_list}",
                          "用例执行结果描述")  # 将实际结果打印到allure报告

    @pytest.mark.usefixtures('set_sheng')
    @allure.story('按年度查询考核--测试用例')
    @pytest.mark.parametrize("year_select", test_year_select_data)  # 将数据传入测试用例
    def test_year_select_assess(self, year_select, log, driver):
        """
        :param year_select:按‘考核年度’查询
        :param log:
        :param driver:
        :return:
        """
        log.logger.info("测试用例：按年度查询考核，开始")
        sleep(5)
        select = PageAssess(driver)
        select.select_by_year(year_select)
        sleep(3)

        # 表格定位路径
        element = driver.find_element(By.CLASS_NAME, "ant-table-tbody")
        result_list = TableDataExtractor.get_column_data(element, 1)
        print(result_list)
        log.logger.info(f"查询到的所有年度为{result_list}")
        b = ""
        for b in result_list:
            print('列表数据遍历完成')
        try:
            assert year_select in b, f"{b}不包含{year_select}"
            log.logger.info(f"考核年度{year_select}查询成功")
        except AssertionError as e:
            msg = f"查询的考核年度为：{year_select},实际查询到的结果为：{result_list}"
            log.logger.error(msg)
            print(f"异常原因：{msg}")  # 打印异常原因
            save_error_screenshot("查询列表断言失败截图", driver, 'select_assess_image')
            raise e  # 抛出异常,否则用例会被判断为pass
        except (NoSuchElementException, exceptions.TimeoutException) as e:  # 如果是没找到元素
            msg = f"元素定位失败，具体错误信息{e}"
            log.logger.error(msg)
            print(f"异常原因：{msg}")  # 打印异常原因
            save_error_screenshot("查询元素定位失败截图", driver, 'select_assess_image')
            pytest.fail(reason="元素定位失败")
        except Exception as e:
            msg = f"其他错误，具体错误信息{e}"
            log.logger.error(msg)
            print(f"异常原因：{msg}")
            save_error_screenshot("查询其他错误截图", driver, 'select_assess_image')
            raise e
        finally:
            log.logger.info(f"测试用例结束，考核年度：{year_select}查询完成")
            allure.attach(driver.get_screenshot_as_png(), "用例执行结果截图",
                          attachment_type=allure.attachment_type.PNG)  # 将用例最终截图打印到allure报告，无论失败与否都打印
            allure.attach(f"查询的考核年度为：{year_select},实际查询到的结果为：{result_list}",
                          "用例执行结果描述")  # 将实际结果打印到allure报告
