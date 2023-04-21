import document as document
from selenium.webdriver.common.by import By

from base.base_page import BasePage


class PageAddFdy(BasePage):
    current_url = "http://192.168.0.40:18400/index#/counsellorManage/counsellorManage"
    add_btn = (By.XPATH,"//body//button[2]")  # 【新增辅导员】按钮
    js = 'document.getElementById("train_date").removeAttribute("readonly")'

