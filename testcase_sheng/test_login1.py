# -*- coding: utf-8 -*-
from time import sleep

import numpy as  np
from selenium.webdriver.common.by import By

import base


def test():
        driver = base.base_page.driver
        driver.get("http://192.168.0.40:18400/index#/login")
        driver.find_element(By.ID,"name").send_keys("hnssgw")
        driver.find_element(By.ID,"password").send_keys("123456")
        sleep(15)
        driver.find_elements(By.CLASS_NAME,"btn-reject")
