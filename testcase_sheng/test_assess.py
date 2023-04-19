"""
省少工委发布考核测试用例
"""
import time
from time import sleep
import allure
import pytest
from selenium.webdriver.common.by import By
from base.base_page import driver
from pageobject.login_page import LoginPage
from pageobject.pagesheng.lzkh_page import LzkhPage

test_publish_data = [("测试新增考核", "2023-04-13", "2023-04-30", "2795123"),
                     ("测试新增考核2", "2023-04-13", "2023-04-30", "2795456")]

test_select_data = ["测试新增考核"]


class TestAssess:
    lp = LoginPage()  # 要先登录
    lp.login_sgw("hnssgw", "123456")  # 先登录

    @allure.story('发布考核--测试用例')
    @pytest.mark.parametrize("kh_name,starttime,endtime,telephone", test_publish_data)  # 将数据传入测试用例
    def test_publish(self, kh_name, starttime, endtime, telephone, log):  # 发布考核
        log.logger.info("测试用例：发布考核，开始")
        sleep(5)
        et = LzkhPage()  # 进行考核发布的操作
        et.publish_lzkh(kh_name, starttime, endtime, telephone)
        time.sleep(3)  # 等待3s，避免加载慢
        text = ""
        try:
            text = driver.find_element(By.XPATH, "//tr[1]//td[3]").text
            assert text == "测试自动输入考核名称"
            log.logger.info(
                "考核名称{0}，开始时间{1}，结束时间{2}，咨询电话{3}发布成功".format(kh_name, starttime, endtime, telephone))
        except Exception as msg:
            msg = "考核名称{0}，开始时间{1}，结束时间{2}，咨询电话{3}断言失败，返回text:{0}".format(kh_name, starttime, endtime, telephone, text)
            log.logger.error(msg)
            now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            print(u"异常原因%s" % msg)  # 打印异常原因
            imgname = now + "异常截图.png"
            # 如果操作步骤过程中有异常，那么用例失败，在这里完成截图操作
            file_path = 'error_image/publish_image/' + imgname
            driver.save_screenshot(file_path)
            # 将截图展示在allure测试报告上
            with open(file_path, mode="rb") as f:
                allure.attach(f.read(), imgname, allure.attachment_type.PNG)
            raise  # 抛出异常,否则用例会被判断为pass
        finally:
            log.logger.info(
                "测试用例结束，考核名称{0}，开始时间{1}，结束时间{2}，咨询电话{3}".format(kh_name, starttime, endtime, telephone))

    @allure.story('按名称查询考核--测试用例')
    @pytest.mark.parametrize("name_select", test_select_data)  # 将数据传入测试用例
    def test_select_assess(self, name_select, log):
        log.logger.info("测试用例：按名称查询考核，开始")
        sleep(5)
        select = LzkhPage()
        select.select_by_name(name_select)
        sleep(3)
        list_1 = []
        # 表格定位路径
        element = driver.find_element(By.CLASS_NAME, "ant-table-tbody")
        # 获取每一行数据tr
        table_tr_list = element.find_elements(By.TAG_NAME, "tr")
        # 按行查询表格的数据，取出的数据是一整行
        for tr in table_tr_list:
            # tr.text获取表格每行的文本内容、切割字符串
            list_2 = tr.text.split()
            list_1.append(list_2)
        #     print(tr.text)
        # print(list_1)
        result_list = [x[2] for x in list_1]
        # print(result_list)
        b = ""
        for b in result_list:
            print('列表数据遍历完成')
        try:
            assert name_select in b, f"{b}不包含{name_select}"
            log.logger.info("考核名称{0}查询成功".format(name_select))
        except Exception as msg:
            msg = "查询的考核名称为：{},市级查询到的结果为：{}:".format(name_select, result_list)
            log.logger.error(msg)
            now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            print(u"异常原因%s" % msg)  # 打印异常原因
            imgname = now + "异常截图.png"
            # 如果操作步骤过程中有异常，那么用例失败，在这里完成截图操作
            file_path = 'error_image/publish_image/' + imgname
            driver.save_screenshot(file_path)
            # 将截图展示在allure测试报告上
            with open(file_path, mode="rb") as f:
                allure.attach(f.read(), imgname, allure.attachment_type.PNG)
            raise  # 抛出异常,否则用例会被判断为pass
        finally:
            log.logger.info("测试用例结束，考核名称：{0}查询完成".format(name_select))
