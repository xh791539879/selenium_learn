"""
省少工委新增履职考核
"""
import time
from time import sleep

import allure
import pytest
from selenium.webdriver.common.by import By

from Util.error_screenshot_util import save_error_screenshot
from pageobject.pagesheng.page_assess import PageAssess

# 测试数据，包括考核年度、考核名称、开始时间、结束时间、咨询电话等信息
test_publish_data = [("2023", "测试新增考核", "2023-05-13", "2023-05-30", "2795123"),
                     ("2021", "测试新增考核2", "2023-05-13", "2023-05-30", "2795456")]


@allure.feature('发布履职考核模块')
class TestAssess:
    """发布考核测试用例"""

    @pytest.mark.usefixtures('set_sheng')
    @allure.story('发布考核--测试用例')
    @pytest.mark.parametrize("year,kh_name,starttime,endtime,telephone", test_publish_data)  # 将数据传入测试用例
    def test_publish(self, year, kh_name, starttime, endtime, telephone, log, driver):  # 获取driver对象，执行测试用例之前必须初始化driver
        """
        测试用例：发布考核
        :param year: 考核年度
        :param kh_name: 考核名称
        :param starttime: 开始时间
        :param endtime: 结束时间
        :param telephone: 咨询电话
        :param log: 日志
        """
        log.logger.info("测试用例：发布考核，开始")
        sleep(5)
        et = PageAssess(driver)  # 进行考核发布的操作
        et.publish_lzkh(year, kh_name, starttime, endtime, telephone)
        time.sleep(3)  # 等待3s，避免加载慢
        text = ""
        try:
            # 尝试在页面中查找考核名称，在第一行第三列
            text = driver.find_element(By.XPATH, "//tr[1]//td[3]").text
            assert text == "测试自动输入考核名称"
            # 断言成功，打印日志
            log.logger.info(
                f"考核年度{year}，考核名称{kh_name}，开始时间{starttime}，结束时间{endtime}，咨询电话{telephone}发布成功")
        except AssertionError as e:
            # 断言失败，打印日志，保存异常截图
            msg = f"考核年度{year}，考核名称{kh_name}，开始时间{starttime}，结束时间{endtime}，咨询电话{telephone}发布断言失败，返回text:{text}"
            log.logger.error(msg)
            print(f"异常原因：{msg}")
            save_error_screenshot("查询列表断言失败截图", driver, 'select_assess_image')
            raise e
        finally:
            # 打印日志
            log.logger.info(
                f"测试用例结束，考核年度{year}，考核名称{kh_name}，开始时间{starttime}，结束时间{endtime}，咨询电话{telephone}")
            allure.attach(driver.get_screenshot_as_png(), "用例执行结果截图",
                          attachment_type=allure.attachment_type.PNG)  # 将用例最终截图打印到allure报告，无论失败与否都打印
            allure.attach(
                f"考核年度{year}，考核名称{kh_name}，开始时间{starttime}，结束时间{endtime}，咨询电话{telephone}操作完成，返回的text:{text}",
                "用例执行结果描述")  # 将实际结果打印到allure报告
