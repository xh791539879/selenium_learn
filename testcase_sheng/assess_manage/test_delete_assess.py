from time import sleep

import allure
import pytest
from selenium.common import NoSuchElementException, exceptions

from Util.error_screenshot_util import save_error_screenshot
from pageobject.pagesheng.page_assess import PageAssess

test_name_select_data = ["������������"]


class TestDeleteAssess:
    @pytest.mark.usefixtures('set_sheng')
    @allure.story('ɾ��--��������')
    @pytest.mark.parametrize("name_select", test_name_select_data)  # �����ݴ����������
    def test_del_assess(self, name_select, log, driver):  # ��ȡdriver����ִ�в�������֮ǰ�����ʼ��driver
        """
        :param name_select:ͨ��'��������'��ѯ��ɾ��
        :param log:��־
        :param driver:����
        :return:��
        """
        log.logger.info("����������ɾ�����ˣ���ʼ")
        sleep(5)
        del_assess = PageAssess(driver)
        title_before, title_after = del_assess.del_table(0)
        print(title_before)
        print(title_after)
        try:
            assert title_after != title_before
            log.logger.info(f"�����Զ������Կ������ƣ�����Ϊ{title_before}����ɾ���ɹ�")
        except AssertionError as e:
            msg = f"ɾ������ʧ�ܣ���Ϊ{title_before}�Ŀ��˻�����"
            log.logger.error(msg)
            print(f"�쳣ԭ��{msg}")  # ��ӡ�쳣ԭ��
            save_error_screenshot("ɾ�����˶���ʧ�ܽ�ͼ", driver, 'delete_assess_image')
            raise e  # �׳��쳣,���������ᱻ�ж�Ϊpass
        except (NoSuchElementException, exceptions.TimeoutException) as e:  # �����û�ҵ�Ԫ��
            msg = f"Ԫ�ض�λʧ�ܣ����������Ϣ{e}"
            log.logger.error(msg)
            print(f"�쳣ԭ��{msg}")  # ��ӡ�쳣ԭ��
            save_error_screenshot("��ѯԪ�ض�λʧ�ܽ�ͼ", driver, 'delete_assess_image')
            pytest.fail(reason="Ԫ�ض�λʧ��")
        except Exception as e:
            msg = f"�������󣬾��������Ϣ{e}"
            log.logger.error(msg)
            print(f"�쳣ԭ��{msg}")
            save_error_screenshot("��ѯ���������ͼ", driver, 'delete_assess_image')
            raise e
        finally:
            log.logger.info(f"��������������������ȣ�{title_before}ɾ�������������")
            allure.attach(driver.get_screenshot_as_png(), "����ִ�н����ͼ",
                          attachment_type=allure.attachment_type.PNG)  # ���������ս�ͼ��ӡ��allure���棬����ʧ����񶼴�ӡ
            allure.attach(f"ɾ���Ŀ�������Ϊ��{title_before},ʵ�ʲ�ѯ���Ľ��Ϊ��{title_after}",
                          "����ִ�н������")  # ��ʵ�ʽ����ӡ��allure����
