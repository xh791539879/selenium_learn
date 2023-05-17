from time import sleep

import allure
import pytest
from selenium.webdriver.common.by import By

from Util.error_screenshot_util import save_error_screenshot
from common.common import TableDataExtractor
from pageobject.pagesheng.page_assess import PageAssess

# �������ݣ���������������
test_name_select_data = ["������������"]
# �������ݣ��������������
test_year_select_data = ["2023"]


class TestSearchAssess:

    # ͨ��fixture������ǰ�����������Զ���¼ϵͳ��������ָ��ҳ��
    @pytest.mark.usefixtures('set_sheng')
    # ����allure�еĲ�����������ͱ���
    @allure.story('�����Ʋ�ѯ����--��������')
    # parametrizeװ�������������ݴ����������
    @pytest.mark.parametrize("name_select", test_name_select_data)
    def test_name_select_assess(self, name_select, log, driver):  # ��ȡdriver����ִ�в�������֮ǰ�����ʼ��driver
        """
        :param name_select:����'��������'��ѯ
        :param log:
        :param driver:
        :return:
        """

        # ��¼��־
        log.logger.info("���������������Ʋ�ѯ���ˣ���ʼ")

        # �ȴ�ҳ��������
        sleep(5)

        # ����PageAssess���󣬵�����Ӧ�ķ������в��Բ���
        select = PageAssess(driver)
        select.select_by_name(name_select)
        sleep(3)

        # ��λ����ѯ�����񣬲�ͨ��TableDataExtractor��ȡ�����ָ���е�����
        element = driver.find_element(By.CLASS_NAME, "ant-table-tbody")
        result_list = TableDataExtractor.get_column_data(element, 2)
        print(result_list)

        b = ""
        for b in result_list:
            print('�б����ݱ������')

        try:
            # �Ի�ȡ�����ݽ��ж��Աȶԣ���֤��ѯ����Ƿ����Ԥ��
            assert name_select in b, f"{b}������{name_select}"
            log.logger.info("��������{0}��ѯ�ɹ�".format(name_select))
        except AssertionError as e:
            # ���������������׳��쳣��ͬʱ�����ֳ���ͼ�������ᱻ�ж�Ϊʧ��
            msg = f"��ѯ�Ŀ�������Ϊ��{name_select},ʵ�ʲ�ѯ���Ľ��Ϊ��{result_list}"
            log.logger.error(msg)
            print(f"�쳣ԭ��{msg}")
            save_error_screenshot("��ѯ�б����ʧ�ܽ�ͼ", driver, 'select_assess_image')
            raise e
        finally:
            # ��¼��־����������ִ�н���
            log.logger.info(f"���������������������ƣ�{name_select}��ѯ���")
            allure.attach(driver.get_screenshot_as_png(), "����ִ�н����ͼ",
                          attachment_type=allure.attachment_type.PNG)  # ���������ս�ͼ��ӡ��allure���棬����ʧ����񶼴�ӡ
            allure.attach(f"��ѯ�Ŀ������Ϊ��{name_select},ʵ�ʲ�ѯ���Ľ��Ϊ��{result_list}",
                          "����ִ�н������")  # ��ʵ�ʽ����ӡ��allure����

    @pytest.mark.usefixtures('set_sheng')
    @allure.story('����Ȳ�ѯ����--��������')
    @pytest.mark.parametrize("year_select", test_year_select_data)  # �����ݴ����������
    def test_year_select_assess(self, year_select, log, driver):
        """
        :param year_select:����������ȡ���ѯ
        :param log:
        :param driver:
        :return:
        """
        log.logger.info("��������������Ȳ�ѯ���ˣ���ʼ")
        sleep(5)
        select = PageAssess(driver)
        select.select_by_year(year_select)
        sleep(3)

        # ���λ·��
        element = driver.find_element(By.CLASS_NAME, "ant-table-tbody")
        result_list = TableDataExtractor.get_column_data(element, 1)
        print(result_list)
        log.logger.info(f"��ѯ�����������Ϊ{result_list}")
        b = ""
        for b in result_list:
            print('�б����ݱ������')
        try:
            assert year_select in b, f"{b}������{year_select}"
            log.logger.info(f"�������{year_select}��ѯ�ɹ�")
        except AssertionError as e:
            msg = f"��ѯ�Ŀ������Ϊ��{year_select},ʵ�ʲ�ѯ���Ľ��Ϊ��{result_list}"
            log.logger.error(msg)
            print(f"�쳣ԭ��{msg}")  # ��ӡ�쳣ԭ��
            save_error_screenshot("��ѯ�б����ʧ�ܽ�ͼ", driver, 'select_assess_image')
            raise e  # �׳��쳣,���������ᱻ�ж�Ϊpass
        except (NoSuchElementException, exceptions.TimeoutException) as e:  # �����û�ҵ�Ԫ��
            msg = f"Ԫ�ض�λʧ�ܣ����������Ϣ{e}"
            log.logger.error(msg)
            print(f"�쳣ԭ��{msg}")  # ��ӡ�쳣ԭ��
            save_error_screenshot("��ѯԪ�ض�λʧ�ܽ�ͼ", driver, 'select_assess_image')
            pytest.fail(reason="Ԫ�ض�λʧ��")
        except Exception as e:
            msg = f"�������󣬾��������Ϣ{e}"
            log.logger.error(msg)
            print(f"�쳣ԭ��{msg}")
            save_error_screenshot("��ѯ���������ͼ", driver, 'select_assess_image')
            raise e
        finally:
            log.logger.info(f"��������������������ȣ�{year_select}��ѯ���")
            allure.attach(driver.get_screenshot_as_png(), "����ִ�н����ͼ",
                          attachment_type=allure.attachment_type.PNG)  # ���������ս�ͼ��ӡ��allure���棬����ʧ����񶼴�ӡ
            allure.attach(f"��ѯ�Ŀ������Ϊ��{year_select},ʵ�ʲ�ѯ���Ľ��Ϊ��{result_list}",
                          "����ִ�н������")  # ��ʵ�ʽ����ӡ��allure����
