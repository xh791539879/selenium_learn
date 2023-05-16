# -*- coding: utf-8 -*-
import random

from info_common.name import *
from info_common.phone import phone_number
from info_common.province import province_id


# 随机生成姓名
def get_name():
    user_name = ''
    # 在百家姓列表里面随便选择一个姓
    user_name += random.choice(first_name)
    ran_num = random.randint(0, 1)
    # 为0生成的名字是两个字,为1生成的名字是一个字
    if ran_num == 0:
        for i in range(2):
            ming = random.choice(second_name)
            user_name += ming
    else:
        ming = random.choice(second_name)
        user_name += ming
    # 编码
    user_name.encode('utf-8')
    return user_name


# 随机生成身份证号
def get_idnum():
    id_num = ''
    # 随机选择地址码
    id_num += str(random.choice(province_id))
    # 随机生成4-6位地址码
    for i in range(4):
        ran_num = str(random.randint(0, 9))
        id_num += ran_num
    b = get_birthday()
    id_num += b
    # 生成15、16位顺序号
    num = ''
    for i in range(2):
        num += str(random.randint(0, 9))
    id_num += num
    # 通过性别判断生成第十七位数字 男单 女双
    s = get_sex()
    print("性别:", s)
    if s == '男':
        # 生成奇数
        seventeen_num = random.randrange(1, 9, 2)
    else:
        seventeen_num = random.randrange(2, 9, 2)
    id_num += str(seventeen_num)
    eighteen_num = str(random.randint(1, 10))
    if eighteen_num == '10':
        eighteen_num = 'X'
    id_num += eighteen_num
    return id_num


# 随机生成出生日期
def get_birthday():
    # 随机生成年月日
    year = random.randint(1960, 2000)
    month = random.randint(1, 12)
    # 判断每个月有多少天随机生成日
    if year % 4 == 0:
        if month in (1, 3, 5, 7, 8, 10, 12):
            day = random.randint(1, 31)
        elif month in (4, 6, 9, 11):
            day = random.randint(1, 30)
        else:
            day = random.randint(1, 29)
    else:
        if month in (1, 3, 5, 7, 8, 10, 12):
            day = random.randint(1, 31)
        elif month in (4, 6, 9, 11):
            day = random.randint(1, 30)
        else:
            day = random.randint(1, 28)
    # 小于10的月份前面加0
    if month < 10:
        month = '0' + str(month)
    if day < 10:
        day = '0' + str(day)
    birthday = str(year) + str(month) + str(day)
    return birthday


# 匿名函数
get_sex = lambda: random.choice(['男', '女'])


# 随机生成手机号
def get_tel():
    tel = ''
    tel += str(random.choice(phone_number))
    ran = ''
    for i in range(8):
        ran += str(random.randint(0, 9))
    tel += ran
    return tel


# 随机生成银行卡号
def get_card_id():
    card_id = '62'
    for i in range(17):
        ran = str(random.randint(0, 9))
        card_id += ran
    return card_id


# 随机生成邮箱
def get_email():
    email_suf = random.choice(['@163.com', '@qq.com', '@126.com', '@sina.com', '@sina.cn', '@soho.com', '@yeah.com'])
    phone = get_tel()
    email = phone + email_suf
    print("手机号:", phone)
    return email

# if __name__ == '__main__':
#     x = get_name()
#     print("姓名:", x)
#     y = get_idnum()
#     print("身份证号:", y)
#     z = get_email()
#     print("邮箱:", z)
#     w = get_card_id()
#     print("银行卡号:", w)
