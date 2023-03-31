#coding=utf-8
import os
from datetime import datetime, date

class DateTime(object):
    @staticmethod
    def get_current_date():
        """获取当前日期"""
        try:
            current_date = date.today()
        except Exception as e:
            raise e
        else:
            return str(current_date)

    @staticmethod
    def get_current_time():
        """获取当前时间"""
        try:
            time = datetime.now()
            current_time = time.strftime('%H_%M_%S')
        except Exception as e:
            raise e
        else:
            return current_time

    @staticmethod
    def create_file_path():
        """创建文件存放路径路径"""
        try:
            file_path = os.path.join("文件路径", DateTime.get_current_date())
            if not os.path.exists(file_path):
                os.makedirs(file_path)  # 生成多级目录
        except Exception as e:
            raise e
        else:
            return file_path

#
# if __name__ == '__main__':
#     print(DateTime.get_current_date())
#     print(DateTime.get_current_time())
#     print(DateTime.create_file_path())
