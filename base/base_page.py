"""
封装selenium中的方法
#基础层
"""
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):  # 实例化时获取浏览器驱动
        """
        初始化浏览器
        :param driver:
        """
        self.driver = driver

    # 跳转页面方法封装
    def get(self, url):
        """
        :param url: 域名
        :return:
        """
        self.driver.get(url)

    # 定位单个元素方法封装，用EC来等待元素加载
    def find_element(self, args):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(args))

    # 定位多个元素方法封装，用EC来等待元素加载
    def find_elements(self, args):
        """
        :param args: by.*合并为字符串
        :return:
        """
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(args))

    # 对输入框进行输入值操作封装
    def send_keys(self, args, value):
        """
        :param args: by.*合并为字符串
        :param value: 发送内容
        :return:
        """
        element = self.find_element(args)  # 先定位元素
        element.clear()  # 清空输入框中的内容
        element.send_keys(value)  # 发送输入值

    # 对元素进行点击操作封装
    def click(self, args):
        element = self.find_element(args)  # 先定位元素
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(args))  # 等待元素可点击
        element.click()  # 对元素进行点击操作

    # 进入框架操作封装
    def in_frame(self, framename):
        self.driver.switch_to.frame(framename)

    # 跳出框架操作封装
    def out_frame(self):
        self.driver.switch_to.default_content()

    # 对下拉选择框进行数据选择封装
    def choice_select(self, args, value):
        sel = Select(self.find_element(args))  # 先定位元素
        sel.select_by_value(str(value))  # 根据传入的值选择下拉框中对应的选项

    # 移除元素的某个属性
    def remove_attribute(self, xpath, attribute):
        element = self.find_element(xpath)  # 先定位元素
        self.driver.execute_script(f"arguments[0].{attribute}=''", element)  # 通过JavaScript执行移除属性操作

    # 对元素进行键盘点击操作
    def click_keys(self):
        action_chains = ActionChains(self.driver)  # 实例化ActionChains对象
        # 按下并释放Enter键，制造“点击”效果
        action_chains.key_up(Keys.ENTER).perform()
        sleep(1)
        action_chains.key_down(Keys.ENTER).perform()

    # 移除元素的属性值
    def remove_att(self, args):
        self.driver.execute_script('', args)

    # 等待单个元素出现
    def wait_for_element_present(self, xpath):
        self.find_element(xpath)

    # 等待多个元素出现
    def wait_for_elements_present(self, xpath):
        self.find_elements(xpath)

    def get_text(self, args):
        """
        获取元素的文本值
        :param args: by.*合并为字符串
        :return: 元素的text
        """
        element = self.find_element(args)  # 先定位元素
        return element.text
