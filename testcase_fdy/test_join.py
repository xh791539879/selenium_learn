# # -*- coding: utf-8 -*-
# import time
# from time import sleep
# import allure
# import pytest
# from selenium.webdriver.common.by import By
# import base.base_page
# from pageobject.login_page import LoginPage
# from pageobject.pagefdy.page_assess_fdy import PageAssessFdy
#
#
# join_data = ['123456']
#
#
# class TestJoinAssess:
#
#     @pytest.mark.usefixtures('set_fdy')
#     @allure.story('辅导员参加考核--测试用例')
#     @pytest.mark.parametrize("assess_name", join_data)
#     def test_join(self, assess_name, log):
#         log.logger.info('辅导员登录成功，测试用例开始')
#         sleep(5)
#         join_assess = PageAssessFdy()
#         join_assess.join_assess(assess_name)
#         text = ''
#         try:
#             target = driver.find_element(By.XPATH, "//body//a[2]")
#             try:
#                 text = target.text
#                 assert text == "考核详情"
#                 log.logger.info("参加考核成功")
#             except Exception as msg:
#                 msg = "断言失败，按钮的实际文案为：{}".format(text)
#                 log.logger.error(msg)
#                 print(u"异常原因%s" % msg)  # 打印异常原因
#                 now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
#                 imgname = now + "异常截图.png"
#                 # 如果操作步骤过程中有异常，那么用例失败，在这里完成截图操作
#                 file_path = 'error_images/join_assess_image/' + imgname
#                 driver.save_screenshot(file_path)
#                 # 将截图展示在allure测试报告上
#                 with open(file_path, mode="rb") as f:
#                     allure.attach(f.read(), imgname, allure.attachment_type.PNG)
#                 raise  # 抛出异常,否则用例会被判断为pass
#         except Exception as msg:
#             msg = "定位失败，没有该元素"
#             now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
#             print(u"异常原因%s" % msg)  # 打印异常原因
#             imgname = now + "异常截图.png"
#             # 如果操作步骤过程中有异常，那么用例失败，在这里完成截图操作
#             file_path = 'error_images/join_assess_image/' + imgname
#             driver.save_screenshot(file_path)
#             # 将截图展示在allure测试报告上
#             with open(file_path, mode="rb") as f:
#                 allure.attach(f.read(), imgname, allure.attachment_type.PNG)
#             return False
#         finally:
#             log.logger.info("名为{}的考核申报测试完成".format(assess_name))
#
