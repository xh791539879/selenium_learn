from time import sleep

from selenium.webdriver.common.by import By

from base.base_page import BasePage


class PageFdy(BasePage):
    # ����
    current_url = "http://192.168.0.40:18400/index#/counsellorManage/counsellorManage"  # ����Ա����ҳ��
    add_btn = (By.XPATH, "//body//button[2]")  # ����������Ա����ť
    fdy_class_input = (By.XPATH,
                       "//div[@class='ant-modal-body']//div[@class='ant-select-selection__rendered']")  # ����Ա����ѡ���
    fdy_class_select = (By.XPATH,
                        "//div[@class='ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft']//li[2]")  # ����Ա����������ѡ��
    fdy_name_input = (By.XPATH, "//div[@class='ant-modal-body']//div[2]//div[2]//div[1]//span[1]//input[1]")  # ���������
    fdy_id_input = (By.XPATH, "//div[3]//div[2]//div[1]//span[1]//input[1]")  # ���֤�������
    ok_btn = (By.XPATH, "//div[@class='ant-modal-footer']//button[@class='ant-btn ant-btn-primary']")  # ȷ�ϰ�ť
    # ��ѯ
    name_input = (By.XPATH, "//div[@class='ant-row']//div[1]//div[1]//div[2]//div[1]//span[1]//input[1]")  # ����ɸѡ��
    number_input = (
        By.XPATH,
        "//div[@class='page-content side fixed']//div[2]//div[1]//div[2]//div[1]//span[1]//input[1]")  # ���֤ɸѡ��
    class_ddb = (By.XPATH,
                 "//div[@class='ant-select ant-select-enabled ant-select-focused']//div[@class='ant-select-selection__rendered']")  # ����Ա���������
    upper_input = (By.XPATH, "//div[4]//div[1]//div[2]//div[1]//span[1]//input[1]")  # �����ٹ�ί�����
    state_ddb = (By.XPATH,
                 "//div[@class='ant-select ant-select-enabled ant-select-focused']//div[@class='ant-select-selection__rendered']")  # ״̬ɸѡ��
    search_btn = (By.XPATH, "//body//button[1]")  # ��ѯ��ť

    def __init__(self, driver):
        super().__init__(driver)
        self.class_ddb_select = None

    def add_fdy(self, name, numbers):
        self.get(self.current_url)  # �л�������Ա����ҳ��
        self.click(self.add_btn)  # �����������Ա��ť
        sleep(1)
        self.click(self.fdy_class_input)  # �������Ա���ѡ���
        self.click(self.fdy_class_select)  # ѡ�񸨵�Ա���
        self.send_keys(self.fdy_name_input, name)  # ����name
        self.send_keys(self.fdy_id_input, numbers)  # ����idcard
        self.click(self.ok_btn)  # ���ȷ��
        self.send_keys(self.name_input, name)  # ��ΪĬ�ϲ��ǰ������˳����������Ҫ��ɸѡ����
        self.click(self.search_btn)  # �����ѯ��ť

    def search_by_name(self, name):
        self.get(self.current_url)
        sleep(1)
        self.send_keys(self.name_input, name)
        self.click(self.search_btn)

    def search_by_idcard(self, number):
        self.get(self.current_url)
        self.send_keys(self.number_input, number)
        self.click(self.search_btn)

    def search_by_class(self, s):
        self.get(self.current_url)
        self.click(self.class_ddb)
        self.class_ddb_select = (By.XPATH,
                                 f"//div[@class='ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft']//li[{s}]")
        self.click(self.class_ddb_select)
        self.click(self.search_btn)
