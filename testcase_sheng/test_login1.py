from time import sleep

from selenium.webdriver.common.by import By
from webdriver_helper import get_webdriver


class Test:
    def test(self):
        self.driver = get_webdriver()
        self.driver.maximize_window()
        self.driver.get("http://192.168.0.40:18400/index#/login")
        self.driver.find_element(By.ID,"name").send_keys("hnssgw")
        self.driver.find_element(By.ID,"password").send_keys("123456")
        sleep(15)
        arr = []
        arr1 = []
        table = self.driver.find_element(By.XPATH,"//tbody[@class='ant-table-tbody']")
        table_tr_list = table.find_elements(By.XPATH,"//tr[]//td[3]")
        for tr in table_tr_list:
            arr1 = tr.text.split("\n")
            arr.append(arr1)
        return arr
