from time import sleep

from selenium.webdriver.common.by import By
from webdriver_helper import get_webdriver

import base.base_page


class Test:
    def test(self):
        self.driver = base.base_page.driver
        self.driver.get("http://192.168.0.40:18400/index#/login")
        self.driver.find_element(By.ID,"name").send_keys("hnssgw")
        self.driver.find_element(By.ID,"password").send_keys("123456")
        sleep(15)
        # 通过标签名获取表格的所有行
        table_tr_list = self.driver.find_elements(By.XPATH,"//table[@class='ant-table-tbody']/tbody/tr/td[position()=1]")
        # 按行查询表格的数据，取出的数据是一整行，按空格分隔每一列的数据
        print(table_tr_list)



