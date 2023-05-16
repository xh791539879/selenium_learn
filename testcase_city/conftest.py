import pytest

from pageobject.login_page import LoginPage


@pytest.fixture(scope="session", autouse=False)
def set_city(driver):
    lp = LoginPage(driver)  # ÒªÏÈµÇÂ¼
    lp.login_platform("zzssgw", "123456")  # ÏÈµÇÂ¼
    yield
    pass
