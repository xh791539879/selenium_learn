# -*- coding: utf-8 -*-
import time
from time import sleep
import allure
import pytest
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
from base.base_page import driver
from common.log import Logger


@pytest.fixture(scope="session")
def log():
    log =Logger('D:\\HNSGW\\log\\run.log',level='info')
    return log

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


def is_visible(args, timeout=10):
    try:
        ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(args), args)
        return True
    except TimeoutError:
        return False


@pytest.fixture(scope="function", autouse=False)
def login_assert():  # 登录部分断言
    pass
    yield
    try:
        text = driver.find_element(By.CLASS_NAME, "name").text
        assert text == "河南省少工委"
        log.logger.info("用户名{0}，密码{1}登录成功".format(user, pw))
    except Exception as msg:
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        print(u"异常原因%s" % msg)  # 打印异常原因
        imgname = now + "异常截图.png"
        # 如果操作步骤过程中有异常，那么用例失败，在这里完成截图操作
        file_path = 'error_image/login_image/' + imgname
        driver.save_screenshot(file_path)
        # 将截图展示在allure测试报告上
        with open(file_path, mode="rb") as f:
            allure.attach(f.read(), imgname, allure.attachment_type.PNG)
        raise  # 抛出异常,否则用例会被判断为pass
