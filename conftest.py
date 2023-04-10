# -*- coding: utf-8 -*-
from time import sleep
import allure
import pytest
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC


from base.base_page import driver
import datetime


# @pytest.hookimpl(tryfirst=True,hookwrapper=True)
# def pytest_runtest_makereport(item,call):
#     outcome = yield
#     rep = outcome.get_result()
#     if rep.when == 'call' and rep.failed:
#         img = BasePage.driver.get_screenshot_as_png()
#         allure.attach(img,'111',allure.attachment_type.PNG)
@pytest.fixture(scope="session", autouse=True)
def open_driver():
    driver.maximize_window()
    driver.implicitly_wait(5)  # 隐性等待
    yield
    driver.close()


@pytest.fixture(scope="function", autouse=True)
def set_function():
    pass
    yield
    sleep(5)


def is_visible(locator,timeout=10):
    try:
        ui.WebDriverWait(driver,timeout).until(EC.visibility_of_element_located(By.CLASS_NAME),locator)
        return True
    except TimeoutError:
        return False
@pytest.fixture(scope="function", autouse=False)
def login_assert():  # 登录部分断言
    # 创建 文件夹的时间
    mkfile_time = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S')
    mkfile_time = 'kbl' + mkfile_time
    pass
    yield
    is_visible('name')
    if True:
        text = driver.find_element(By.CLASS_NAME, "name").text
        try:
            assert text == "河南省少工委"
        except Exception as msg:
            print(u"异常原因%s" % msg)  # 打印异常原因
            # 如果操作步骤过程中有异常，那么用例失败，在这里完成截图操作
            file_path = 'error_image/' + mkfile_time + '/' + '登录失败截图.png'
            driver.save_screenshot(file_path)
            # 将截图展示在allure测试报告上
            with open(file_path, mode="rb") as f:
                allure.attach(f.read(), "登录失败截图.png", allure.attachment_type.PNG)
            raise  # 抛出异常,否则用例会被判断为pass
    else:
        raise
