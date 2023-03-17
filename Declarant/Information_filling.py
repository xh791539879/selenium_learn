from time import sleep
from webdriver_helper import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By



chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
driver = get_webdriver(options=chrome_options)
driver.get('http://192.168.0.40:18700/#/login')
sleep(1)
# driver.find_element(by=By.ID,value='name').send_keys('130203202303016830')
# driver.find_element(by=By.ID,value='password').send_keys('123456')
# sleep(1)
# driver.find_element(by=By.TAG_NAME,value='button').click()
# sleep(5)
# driver.find_element(by=By.TAG_NAME,value='button').click()
# sleep(1)
# driver.find_element(by=By.XPATH,value='//button[@class="ant-btn ant-btn-primary"]').click()
# driver.find_element(by=By.NAME,value='title').send_keys('')
# driver.find_element(by=By.NAME,value='name').send_keys('')
# driver.find_element(by=By.NAME,value='unitName').send_keys('')

