import allure
import pytest
from selenium.common import exceptions, NoSuchElementException
from selenium.webdriver.common.by import By

from Util.error_screenshot_util import save_error_screenshot
from pageobject.pagecity.page_add_fdy import PageFdy

test_name_data = ['֣�ݶ��ж�']


@allure.feature('��ѯ����Աģ��')
class TestSearchFdy:
    @allure.story('��������ѯ����Ա--��������')
    @pytest.mark.usefixtures('set_city')
    @pytest.mark.parametrize('name', test_name_data)
    def test_search_by_name(self, log, driver, name):
        log.logger.info("������������������ѯ����Ա����ʼ")
        pf = PageFdy(driver)
        pf.search_by_name(name)
        try:
            fdy_name = driver.find_element(By.XPATH, "//tr[1]//td[2]").text
            assert fdy_name == name
            log.logger.info(f"ͨ��������ѯ����Ա��{name}����ѯ�ɹ�������ͨ��")
        except AssertionError as e:
            msg = f"ͨ��������ѯ����Ա��{name}����ѯʧ�ܣ�����ʧ��"
            log.logger.error(msg)
            save_error_screenshot("��ѯ����Ա����ʧ�ܽ�ͼ", driver, 'search_fdy_images')
            raise e
        except (NoSuchElementException, exceptions.TimeoutException) as e:  # �����û�ҵ�Ԫ��
            msg = f"Ԫ�ض�λʧ�ܣ����������Ϣ{e}"
            log.logger.error(msg)
            print(f"�쳣ԭ��{msg}")  # ��ӡ�쳣ԭ��
            save_error_screenshot("��¼Ԫ�ض�λʧ�ܽ�ͼ", driver, 'search_fdy_images')
            pytest.fail(reason="Ԫ�ض�λʧ��")
        except Exception as e:
            msg = f"�������󣬾��������Ϣ{e}"
            log.logger.error(msg)
            print(f"�쳣ԭ��{msg}")
            save_error_screenshot("��ѯ����Ա���������ͼ", driver, 'search_fdy_images')
            raise e
        finally:
            log.logger.info(f"��������ִ�н�������������ѯ����Ա��{name}����ѯ���")
            allure.attach(driver.get_screenshot_as_png(), "����ִ�н����ͼ",
                          attachment_type=allure.attachment_type.PNG)
            allure.attach(f"��������ִ�н�������������ѯ����Ա��{name}����ѯ���")
