import os
import time

from selenium.webdriver.common.by import By
from base.base_page import BasePage


class LzkhPage(BasePage):
    khgl_tab = (By.XPATH, "//li[2]//div[1]")
    Lzkh_tab = (By.LINK_TEXT, "履职考核")
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
                "//div[@class='ant-form-item-control has-error']//div[@class='ant-select-selection__placeholder']")  # 考核年度选择
    year_2023 = (By.XPATH,"//div[contains(text(),'2023')]")
    name_input = (
    By.XPATH, "//div[@class='ant-form-item-control has-error']//input[@placeholder='请输入考核名称']")  # 考核名称输入框
    people_sel = (By.XPATH,
                  "//div[@class='ant-select-selection ant-select-selection--multiple']//div[@class='ant-select-selection__placeholder']")  # 考核人群选择
    people_dd = (By.XPATH,"//div[@class='ant-select-selection__choice__content']")[0]
    start_time_input = (By.XPATH, "//input[@placeholder='开始时间']")
    end_time_input = (By.XPATH, "//input[@placeholder='结束时间']")

    upload_btn = (By.XPATH, "//span[@class='ant-upload']//button[@class='ant-btn']")  # 选择文件
    tel_input = (By.XPATH, "//input[@placeholder='请输入咨询电话']")  # 咨询电话

    def edit_lzkh(self):

        self.click(self.khgl_tab) #点击考核管理TAB
        self.click(self.Lzkh_tab)#点击履职考核TAB
        self.click(self.publish_btn)#点击发布考核按钮
        self.click(self.year_sel)#点击考核年度选择框
        self.click(self.year_2023)#选择2023年度
        self.send_keys(self.name_input,'111') #输入考核名称
        self.click(self.people_sel)#点击人群选择
        self.click(self.people_dd)

        self.click(self.upload_btn)
        time.sleep(3)
        os.system("C:/Users/admin/Desktop/upload.exe")


        # self.remove_readonly(self.start_time_input)
        # self.remove_readonly(self.end_time_input)
