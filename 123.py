# -*- coding: utf-8 -*-
import sys

sys.path.append('common')

from common.makeinfo import get_name, get_idnum

x = get_name()
print("姓名:", x)
y = get_idnum()
print("身份证号:", y)
