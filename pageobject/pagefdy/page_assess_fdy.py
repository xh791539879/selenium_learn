import os
import time
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class PageAssessFdy(BasePage):
    current_url = "http://192.168.0.40:18400/index#/assessment/apply"
    name_select = (By.CLASS_NAME, "ant-input")  # ��������ɸѡ��
    select_btn = (
        By.XPATH,
        "//div[@class='ant-col ant-col-sm-24 ant-col-md-6']//button[@class='ant-btn ant-btn-primary']")  # ����ѯ��ť��
    join_btn = (By.CLASS_NAME, "btn-success")  # ���μӿ��ˡ���ť
    choice_btn = (By.XPATH, "//span[@class='ant-upload']//button[@class='ant-btn']")  # �ϴ�������ť
    ok_btn = (By.XPATH, "//div[@class='ant-modal-footer']//div//button[@class='ant-btn ant-btn-primary']")  # ��ȷ�ϡ���ť

    def join_assess(self, title_text):
        self.get(self.current_url)
        time.sleep(1)
        self.send_keys(self.name_select, title_text)
        time.sleep(1)
        self.click(self.select_btn)
        time.sleep(1)
        self.click(self.join_btn)
        time.sleep(1)
        self.click(self.choice_btn)
        time.sleep(2)
        os.system("C:/Users/admin/Desktop/upload.exe")
        time.sleep(1)
        self.click(self.ok_btn)
        time.sleep(3)
