
import allure
import pytest
from pageobject.pagecity.page_add_fdy import PageAddFdy

test_add_fdy_data = [2]


@allure.feature('新增辅导员模块')
class TestAddFdy:
    @allure.story('新增辅导员测试用例')
    @pytest.mark.usefixtures('set_city')
    @pytest.mark.parametrize("num", test_add_fdy_data)
    def test_add_fdy(self, num, log):
        log.logger.info("测试用例：新增辅导员，开始")
        af = PageAddFdy()
        af.add_fdy(num)
        print(num)
