"""
封装selenium中的方法
#基础层
"""
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from webdriver_helper import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

driver = get_webdriver()

class BasePage:
    def __init__(self):  #
        self.driver = driver

    def get(self, url):  # 跳转地址封装
        self.driver.get(url)

    def locator_element(self, args):  # 定位元素封装将By. name和value看成一个元组
        return self.driver.find_element(*args)

    def send_keys(self, args, value):  # 发送值封装先定位元素
        self.locator_element(args).send_keys(value)

    def click(self, args):  # 点击事件封装,先定位元素
        self.locator_element(args).click()

    def goin_frame(self, framename):  # 进入框架封装
        self.driver.switch_to.frame(framename)

    def out_frame(self):  # 跳出框架封装
        self.driver.switch_to.default_content()

    def choice_select(self, args, value):  # 标准的select标签下拉框封装
        sel = Select(self.locator_element(args))
        sel.select_by_value(str(value))

    def remove_readonly(self, args):
        a = self.locator_element(args)
        self.driver.execute_script('arguments[0].removeAttribute(\"readonly\")', a)

    def click_keys(self):
        action_chains = ActionChains(self.driver)
        action_chains.key_up(Keys.ENTER).perform()
        sleep(1)
        action_chains.key_down(Keys.ENTER).perform()

    def remove_att(self, args):
        self.driver.execute_script('', args)

    def get_table_content(self,args,args2):
        arr = []
        arr1 = []
        table = self.locator_element(args)
        table_tr_list = table.find_elements(args2)
        for tr in table_tr_list:
            arr1 = tr.text.split(" ")
            print(arr1)
            arr.append(arr1)
        return arr
