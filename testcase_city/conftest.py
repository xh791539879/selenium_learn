import pytest
from pageobject.login_page import LoginPage


@pytest.fixture(scope="session", autouse=False)
def set_city():
    lp = LoginPage()  # Ҫ�ȵ�¼
    lp.login_platform("zzssgw", "123456")  # �ȵ�¼
    yield
    pass
