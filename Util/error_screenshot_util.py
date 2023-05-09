import os

import allure  # 导入 allure 库，用于生成测试报告
import time  # 导入 time 库，用于获取当前时间戳


def save_error_screenshot(file_name, driver, sub_folder=""):
    """
    针对自动化测试中的异常情况，将当前浏览器页面截图保存，并添加到 allure 报告中。
    :param file_name: 文件名，描述截图内容
    :param driver: webdriver 实例化的浏览器驱动对象
    :param sub_folder: 截图文件的二级子目录，用于更好的分类管理，默认为空
    :return: 返回截图文件的完整路径
    """
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))  # 获取当前本地时间并格式化
    folder_path = os.path.join('error_images', sub_folder)
    if sub_folder and not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_path = os.path.join('error_images', sub_folder, f"{file_name}_{now}.png")
    driver.save_screenshot(file_path)  # 保存截图
    with open(file_path, mode="rb") as f:  # 打开截图文件，以二进制读取的方式
        allure.attach(f.read(), file_name, allure.attachment_type.PNG)  # 将截图文件添加到 allure 报告中，指定附件类型为 PNG 格式
    return file_path
