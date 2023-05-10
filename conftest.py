# -*- coding: utf-8 -*-
import time
from time import sleep

import pytest
from selenium import webdriver

from common.log import Logger


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # 在fixture结束后销毁driver对象
    driver.quit()


@pytest.fixture(scope="session")
def log():  # 生成日志
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    log = Logger('D:\\workspace-python\\HNSGW\\log\\' + now + 'run.log', level='info')
    return log


@pytest.fixture(scope="function", autouse=True)
def set_function():
    pass
    yield
    sleep(5)
