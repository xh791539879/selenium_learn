# -*- coding: utf-8 -*-
import time
from time import sleep

import allure
import pytest
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
from common.log import Logger


@pytest.fixture(scope="session")
def log():  # 生成日志
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    log = Logger('D:\\HNSGW\\log\\' + now + 'run.log', level='info')
    return log


@pytest.hookimpl(hookwrapper=True, tryfirst=True)  # 修改插件优先级让其首先运行，并保证测试结束后截图能够成功保存
def pytest_exception_interact(node, call, report, driver):
    if node.get_closest_marker('screenshot') is not None and report.failed:
        # 添加一个 name 变量，表示当前用例名称
        name = report.nodeid.replace("::", "_").replace("/", "_")
        file_name = f"{name}_{time.strftime('%Y%m%d-%H%M%S', time.localtime())}.png"
        driver.save_screenshot(f'error_image/{file_name}')
        with open(f'error_image/{file_name}', mode="rb") as f:
            file = f.read()
        allure.attach(file, attachment_type=allure.attachment_type.PNG)


@pytest.fixture(scope="session", autouse=True)
def open_driver(driver):  # 打开浏览器
    driver.maximize_window()
    driver.implicitly_wait(5)  # 隐性等待
    yield
    driver.close()


@pytest.fixture(scope="function", autouse=True)
def set_function():
    pass
    yield
    sleep(5)


# def is_visible(args, timeout=10):
#     try:
#         ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(args), args)
#         return True
#     except TimeoutError:
#         return False

# def pytest_collection_modifyitems(items):
#     """
#     测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
#     :return:
#     """
#     for item in items:
#         item.name = item.name.encode("utf-8").decode("unicode_escape")
#         item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
