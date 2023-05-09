from selenium.webdriver.common.by import By


class TableDataExtractor:
    @staticmethod
    def get_column_data(table_element, col_index):
        """
        获取表格数据，返回指定列的列表
        :param table_element: 表格元素对象
        :param col_index: 列索引，从0开始
        :return: 包含指定列数据的列表
        """
        # 使用 TAG_NAME 找到所有行元素
        table_tr_list = table_element.find_elements(By.TAG_NAME, "tr")

        result_list = []

        # 遍历行元素，逐一获取每行的文本内容
        for tr in table_tr_list:
            # 使用 text 属性获取文本内容，并使用 split() 方法分割字符串
            list_2 = tr.text.split()
            if len(list_2) > col_index:
                result_list.append(list_2[col_index])

        return result_list
