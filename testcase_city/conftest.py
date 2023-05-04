import pytest
from pageobject.login_page import LoginPage


@pytest.fixture(scope="session", autouse=False)
def set_city():
    lp = LoginPage()  # ÒªÏÈµÇÂ¼
    lp.login_platform("zzssgw", "123456")  # ÏÈµÇÂ¼
    yield
    pass
