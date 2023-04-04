from time import sleep

import allure
import pytest
from base.base_page import BasePage, driver


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
    driver.implicitly_wait(5)  # ÒþÐÔµÈ´ý
    yield
    driver.close()
@pytest.fixture(scope="function", autouse=True)
def set_function():
    pass
    yield
    sleep(5)

