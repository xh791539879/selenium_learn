
from time import sleep
from webdriver_helper import *
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestInfor:
    def test_login(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
        driver = get_webdriver(options=chrome_options)
        driver.get('http://192.168.0.40:18700/#/login')
        sleep(1)
        driver.find_element(by=By.ID,value='name').send_keys('130203202303016830')
        driver.find_element(by=By.ID,value='password').send_keys('123456')
        sleep(1)
        driver.find_element(by=By.TAG_NAME,value='button').click()
        sleep(5)
        msg = driver.find_element(by=By.CLASS_NAME,value='title').text
        assert msg =="课题申报"