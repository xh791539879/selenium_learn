import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)
d ="document.getElementByClassName('ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft')[0].removeAttribute('display: none');"
driver.execute_script(d)
time.sleep(1)
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/ul[1]/li[2]").click()