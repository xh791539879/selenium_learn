import pytest

from pageobject.login_page import LoginPage


@pytest.fixture(scope="session", autouse=False)
def set_fdy():
    login_fdy = LoginPage()
    login_fdy.login_platform('140303202301302515', '123456')
    yield
    pass
