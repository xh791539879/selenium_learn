import os
import time

from selenium.webdriver.common.by import By
from base.base_page import BasePage


class LzkhPage(BasePage):
    current_url = "http://192.168.0.40:18400/index#/assessment/year"  # url
    fbkh_btn = (By.CLASS_NAME, "ant-btn ant-btn-danger")  # 发布考核按钮
    selet_btn = (By.CLASS_NAME, "ant-btn ant-btn-primary")  # 查询按钮
    reset_btn = (By.CLASS_NAME, "ant-btn")  # 重置按钮
    year_choice = (By.XPATH,
                   "//div[@class='ant-row']//div[1]//div[1]//div[2]//div[1]//span[1]//div[1]//div[1]//div[1]//div[1]")  # 年度筛选框
    name_btn = (By.XPATH,
                "//input[@placeholder='请输入考核名称']")  # 考核名称筛选框
    people_choice = (By.XPATH,
                     "//div[@class='ant-tabs-content ant-tabs-content-no-animated ant-tabs-top-content ant-tabs-card-content']//div[3]//div[1]//div[2]//div[1]//span[1]//div[1]//div[1]//div[1]//div[1]")  # 考核人群筛选框
    del_btns = (By.LINK_TEXT, "删除")  # 删除按钮
    publish_btn = (By.XPATH, "//button[@class='ant-btn ant-btn-danger']")  # 发布考核按钮
    year_sel = (By.XPATH,
                "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[2]/div[1]/span[1]/div[1]/div[1]/div[1]/div[1]")  # 考核年度选择
    year_2023 = (By.XPATH, "//li[contains(text(),'2023')]")
    js = 'document.getElementByClassName("ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft").removeAttribute("display: none")'
    name_input = (
        By.XPATH,
        "//div[@class='ant-col ant-col-15 ant-form-item-control-wrapper']//input[@placeholder='请输入考核名称']")  # 考核名称输入框
    time_select = (By.XPATH, "//input[@placeholder='开始时间']")
    start_time_input = (By.XPATH, "//div[@class='ant-calendar-date-input-wrap']//input[@placeholder='开始时间']")
    end_time_input = (By.XPATH, "//div[@class='ant-calendar-date-input-wrap']//input[@placeholder='结束时间']")
    upload_btn = (By.XPATH, "//span[@class='ant-upload']//button[@class='ant-btn']")  # 选择文件
    tel_input = (By.XPATH, "//input[@placeholder='请输入咨询电话']")  # 咨询电话

    def edit_lzkh(self, js):
        self.get(self.current_url)
        time.sleep(1)
        self.click(self.publish_btn)  # 点击发布考核按钮
        self.click(self.year_sel)  # 点击考核年度选择框
        self.removeJs = js
        self.click(self.year_2023)  # 选择2023年度
        self.send_keys(self.name_input, '测试自动输入考核名称')  # 输入考核名称
        self.click(self.time_select)  # 点击时间选择控件
        self.send_keys(self.start_time_input, "2023-01-01")
        self.send_keys(self.end_time_input, "2023-04-01")
        self.click(self.upload_btn)
        time.sleep(3)
        os.system("C:/Users/admin/Desktop/upload.exe")  # 调用本地Autolt生成的exe文件进行上传文件操作

        # self.remove_readonly(self.start_time_input)
        # self.remove_readonly(self.end_time_input)
