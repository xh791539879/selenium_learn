# -*- coding: utf-8 -*-
from time import sleep

import numpy as np
from selenium.webdriver.common.by import By

import base


class TestQwer:

    def test_qwer(self):
        self.driver = base.base_page.driver
        self.driver.get("http://192.168.0.40:18400/index#/login")
        self.driver.find_element(By.ID, "name").send_keys("zzssgw")
        self.driver.find_element(By.ID, "password").send_keys("123456")
        sleep(15)
        js = 'document.getElementByClassName("ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft").removeAttribute("display: none;")'
        self.driver.execute_script(js)
        self.driver.find_element(By.XPATH, "//div[@class='ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft']//li[2]")
