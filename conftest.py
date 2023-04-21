# -*- coding: utf-8 -*-
import time
from time import sleep
import pytest
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC

from base.base_page import driver
from common.log import Logger


@pytest.fixture(scope="session")
def log():  # 生成日志
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    log = Logger('D:\\HNSGW\\log\\' + now + 'run.log', level='info')
    return log


@pytest.fixture(scope="session", autouse=True)
def open_driver():  # 打开浏览器
    driver.maximize_window()
    driver.implicitly_wait(5)  # 隐性等待
    yield
    driver.close()


@pytest.fixture(scope="function", autouse=True)
def set_function():
    pass
    yield
    sleep(5)


def is_visible(args, timeout=10):
    try:
        ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(args), args)
        return True
    except TimeoutError:
        return False


# def pytest_collection_modifyitems(items):
#     """
#     测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
#     :return:
#     """
#     for item in items:
#         item.name = item.name.encode("utf-8").decode("unicode_escape")
#         item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
