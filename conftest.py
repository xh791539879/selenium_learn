# -*- coding: utf-8 -*-
import time
from time import sleep
import pytest
from common.log import Logger


@pytest.fixture(scope="session")
def log():  # 生成日志
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    log = Logger('D:\\HNSGW\\log\\' + now + 'run.log', level='info')
    return log


@pytest.fixture(scope="function", autouse=True)
def set_function():
    pass
    yield
    sleep(5)


