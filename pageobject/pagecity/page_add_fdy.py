from time import sleep

from selenium.webdriver.common.by import By

from base.base_page import BasePage


class PageFdy(BasePage):
    # 新增
    current_url = "http://192.168.0.40:18400/index#/counsellorManage/counsellorManage"  # 辅导员管理页面
    add_btn = (By.XPATH, "//body//button[2]")  # 【新增辅导员】按钮
    fdy_class_input = (By.XPATH,
                       "//div[@class='ant-modal-body']//div[@class='ant-select-selection__rendered']")  # 辅导员类型选择框
    fdy_class_select = (By.XPATH,
                        "//div[@class='ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft']//li[2]")  # 辅导员类型下拉框选择
    fdy_name_input = (By.XPATH, "//div[@class='ant-modal-body']//div[2]//div[2]//div[1]//span[1]//input[1]")  # 姓名输入框
    fdy_id_input = (By.XPATH, "//div[3]//div[2]//div[1]//span[1]//input[1]")  # 身份证号输入框
    ok_btn = (By.XPATH, "//div[@class='ant-modal-footer']//button[@class='ant-btn ant-btn-primary']")  # 确认按钮
    # 查询
    name_input = (By.XPATH, "//div[@class='ant-row']//div[1]//div[1]//div[2]//div[1]//span[1]//input[1]")  # 姓名筛选框
    number_input = (
        By.XPATH,
        "//div[@class='page-content side fixed']//div[2]//div[1]//div[2]//div[1]//span[1]//input[1]")  # 身份证筛选框
    class_ddb = (By.XPATH,
                 "//div[@class='ant-select ant-select-enabled ant-select-focused']//div[@class='ant-select-selection__rendered']")  # 辅导员类别下拉框
    upper_input = (By.XPATH, "//div[4]//div[1]//div[2]//div[1]//span[1]//input[1]")  # 所属少工委输入框
    state_ddb = (By.XPATH,
                 "//div[@class='ant-select ant-select-enabled ant-select-focused']//div[@class='ant-select-selection__rendered']")  # 状态筛选框
    search_btn = (By.XPATH, "//body//button[1]")  # 查询按钮

    def __init__(self, driver):
        super().__init__(driver)
        self.class_ddb_select = None

    def add_fdy(self, name, numbers):
        self.get(self.current_url)  # 切换到辅导员管理页面
        self.click(self.add_btn)  # 点击新增辅导员按钮
        sleep(1)
        self.click(self.fdy_class_input)  # 点击辅导员类别选择框
        self.click(self.fdy_class_select)  # 选择辅导员类别
        self.send_keys(self.fdy_name_input, name)  # 输入name
        self.send_keys(self.fdy_id_input, numbers)  # 输入idcard
        self.click(self.ok_btn)  # 点击确认
        self.send_keys(self.name_input, name)  # 因为默认不是按照添加顺序排序，所以要先筛选出来
        self.click(self.search_btn)  # 点击查询按钮

    def search_by_name(self, name):
        self.get(self.current_url)
        sleep(1)
        self.send_keys(self.name_input, name)
        self.click(self.search_btn)

    def search_by_idcard(self, number):
        self.get(self.current_url)
        self.send_keys(self.number_input, number)
        self.click(self.search_btn)

    def search_by_class(self, s):
        self.get(self.current_url)
        self.click(self.class_ddb)
        self.class_ddb_select = (By.XPATH,
                                 f"//div[@class='ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft']//li[{s}]")
        self.click(self.class_ddb_select)
        self.click(self.search_btn)
