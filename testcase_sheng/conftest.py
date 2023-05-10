import pytest
from pageobject.login_page import LoginPage

@pytest.fixture(scope="session", autouse=False)
def set_sheng(driver):
    lp = LoginPage(driver)  # Ҫ�ȵ�¼
    lp.login_platform("hnssgw", "123456")  # �ȵ�¼
    yield
    pass
