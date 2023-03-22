from time import sleep

from selenium.webdriver.support.select import Select
from webdriver_helper import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestInfor:
    def test_login(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
        driver = get_webdriver(options=chrome_options)
        driver.get('http://192.168.0.40:18400/index#/login')
        sleep(1)
        driver.find_element(By.ID, 'name').send_keys('hnssgw')
        driver.find_element(By.ID, 'password').send_keys('123456')
        sleep(1)
        driver.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-primary login-btn ant-btn-lg']").click()
        sleep(5)
        driver.find_element(By.XPATH, "//li[2]//div[1]").click()
        sleep(1)
        driver.find_element(By.LINK_TEXT, "履职考核").click()

    def test_delete(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
        driver = get_webdriver(options=chrome_options)
        driver.get('http://192.168.0.40:18400/index#/login')
        sleep(1)
        driver.find_element(By.ID, 'name').send_keys('hnssgw')
        driver.find_element(By.ID, 'password').send_keys('123456')
        sleep(1)
        driver.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-primary login-btn ant-btn-lg']").click()
        sleep(5)
        driver.find_element(By.XPATH, "//li[2]//div[1]").click()
        sleep(1)
        driver.find_element(By.LINK_TEXT, "履职考核").click()
        sleep(1)
        driver.find_elements(By.LINK_TEXT, "删除")[0].click()
        sleep(1)
        driver.find_element(By.XPATH,
                            "//div[@class='ant-modal-confirm-btns']//button[@class='ant-btn ant-btn-danger']").click()
