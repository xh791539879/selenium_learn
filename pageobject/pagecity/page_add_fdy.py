import document as document
from selenium.webdriver.common.by import By

from base.base_page import BasePage


class PageAddFdy(BasePage):
    current_url = "http://192.168.0.40:18400/index#/counsellorManage/counsellorManage"
    add_btn = (By.XPATH,"//body//button[2]")  # 【新增辅导员】按钮
    fdy_class_input = (By.XPATH,"//div[@class='ant-select ant-select-enabled ant-select-focused']//div[@class='ant-select-selection__rendered']")
    fdy_class = (By.XPATH,"//div[@class='ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft']//li[%s]")

    def add_fdy(self, s):
        self.get(self.current_url)
        self.click(self.add_btn)
        self.click(self.fdy_class_input)
        self.click(self.fdy_class[1] % s)


