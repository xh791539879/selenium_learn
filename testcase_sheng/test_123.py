# -*- coding: utf-8 -*-
from time import sleep

import numpy as np
from selenium.webdriver.common.by import By

import base
from base import base_page


class TestQwer:

    def test_qwer(self):
        self.driver = base_page.driver
        self.driver.get("http://192.168.0.40:18400/index#/login")
        self.driver.find_element(By.ID, "name").send_keys("zzssgw")
        self.driver.find_element(By.ID, "password").send_keys("123456")
        sleep(30)

        # js = "document.getElementsByClassName('ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft')[0].style.display='block'"
        # self.driver.execute_script(js)
        # sleep(3)
        self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[2]/div[1]/span[1]/div[1]/div[1]/div[1]").click()
        sleep(2)
        self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[2]").click()
        self.driver.find_element(By.XPATH, "//div[@class='ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft']//li[2]").click()

