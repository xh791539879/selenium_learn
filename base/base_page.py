
"""
封装selenium中的方法
"""

from webdriver_helper import *
from selenium.webdriver.chrome.options import Options

class BasePage:
    def open_browser(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
        self.driver = get_webdriver(options=self.chrome_options)
        self.driver.implicitly_wait(5)  # 隐性等待

    def get(self, url):
        self.driver.get(url)

    def locator_element(self, args):
        return self.driver.find_element(*args)  # 将By. name和value看成一个元组

    def send_keys(self, args, value):
        self.locator_element(args).send_keys(value)

    def click(self, args):
        self.locator_element(args).click()
