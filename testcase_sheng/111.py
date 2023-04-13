#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
driver = webdriver.Chrome(options=chrome_options)
# 获取列表全部数据
def get_table_content():
    a =  driver.find_element(By.CLASS_NAME,"name").text
    print(a)