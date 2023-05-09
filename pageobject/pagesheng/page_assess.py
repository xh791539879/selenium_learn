"""
省少工委发布考核功能
"""
import os
import time
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class PageAssess(BasePage):  # 定位需要的元素
    current_url = "http://192.168.0.40:18400/index#/assessment/year"  # url
    select_btn = (By.XPATH,
                  "/html[1]/body[1]/div[1]/section[1]/section[1]/main[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[4]/span[1]/button[1]")  # 查询按钮
    reset_btn = (By.CLASS_NAME, "ant-btn")  # 重置按钮
    year_choice = (By.XPATH,
                   "//div[@class='ant-row']//div[1]//div[1]//div[2]//div[1]//span[1]//div[1]//div[1]//div[1]//div[1]")  # 年度筛选框
    name_select = (By.XPATH,
                   "//input[@placeholder='请输入考核名称']")  # 考核名称筛选框
    people_choice = (By.XPATH,
                     "//div[@class='ant-tabs-content ant-tabs-content-no-animated ant-tabs-top-content ant-tabs-card-content']//div[3]//div[1]//div[2]//div[1]//span[1]//div[1]//div[1]//div[1]//div[1]")  # 考核人群筛选框
    del_btns = (By.LINK_TEXT, "删除")  # 第一个删除按钮
    publish_btn = (By.XPATH, "//button[@class='ant-btn ant-btn-danger']")  # 发布考核按钮
    year_click = (By.XPATH,
                  "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/form[1]/div[1]/div[2]/div[1]/span[1]/div[1]/div[1]/div[1]")  # 考核年度选择（发布）
    name_input = (
        By.XPATH,
        "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/form[1]/div[2]/div[2]/div[1]/span[1]/input[1]")  # 考核名称输入框
    time_select = (By.XPATH, "//input[@placeholder='开始时间']")
    start_time_input = (By.XPATH, "//div[@class='ant-calendar-date-input-wrap']//input[@placeholder='开始时间']")
    end_time_input = (By.XPATH, "//div[@class='ant-calendar-date-input-wrap']//input[@placeholder='结束时间']")
    upload_btn = (By.XPATH, "//span[@class='ant-upload']//button[@class='ant-btn']")  # 选择文件
    tel_input = (By.XPATH, "//input[@placeholder='请输入咨询电话']")  # 咨询电话
    ok_btn = (By.XPATH, "//div[@class='ant-modal-footer']//div//button[@class='ant-btn ant-btn-primary']")
    js = (By.XPATH, "//body/div[@id='popContainer']/div[1]/div[1]/div[1]")

    def publish_lzkh(self, year_str, kh_name, starttime, endtime, telephone):  # 发布履职考核

        self.get(self.current_url)
        time.sleep(1)
        self.click(self.publish_btn)  # 点击发布考核按钮
        time.sleep(2)
        self.click(self.year_click)  # 点击考核年度选择框
        time.sleep(1)  # 手动选择年度
        self.year_select = (By.XPATH, "//li[contains(text(),'%s')]" % year_str)  # 将年度选择框插入变量，可以自定义选择
        self.click(self.year_select)
        time.sleep(1)
        self.send_keys(self.name_input, kh_name)  # 输入考核名称
        self.click(self.time_select)  # 点击时间选择控件
        time.sleep(2)
        self.send_keys(self.start_time_input, starttime)  # 开始时间
        time.sleep(1)
        self.send_keys(self.end_time_input, endtime)  # 结束时间
        self.click_keys()  # 单击键盘回车键,让时间控件收回
        self.click(self.upload_btn)
        time.sleep(3)
        os.system("C:/Users/admin/Desktop/upload.exe")  # 调用本地Autolt生成的exe文件进行上传文件操作
        time.sleep(2)
        self.send_keys(self.tel_input, telephone)
        time.sleep(1)
        self.click(self.ok_btn)

    def select_by_name(self, name_select):  # 根据考核名称筛选
        self.get(self.current_url)
        self.send_keys(self.name_select, name_select)
        time.sleep(2)
        self.click(self.select_btn)
        time.sleep(2)

    def select_by_year(self, year_str):
        self.get(self.current_url)
        self.click(self.year_choice)
        self.year_select = (By.XPATH, "//li[contains(text(),'%s')]" % year_str)  # 将年度选择框插入变量，可以自定义选择
        self.click(self.year_select)
        self.click(self.select_btn)
        time.sleep(2)

    def del_table(self, number):
        self.get(self.current_url)
        time.sleep(2)
        self.s_click(self.del_btns, number)  # 获取界面所有删除按钮，定位到第几个为变量，用例层传参
        time.sleep(1)
        self.click_keys()
