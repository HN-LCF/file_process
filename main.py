# -*- coding: utf-8 -*-
"""
@File       :main.py
@Time       :2021/3/18 22:38
@Author     :HN-LCF
@Email      :lou666888out@163.com
@Software   :PyCharm
"""

# todo:
#   -

from src import image_resize as ir

print("Start:\n")
file_path = './data/photos/'
file_name = 'lcf.jpg'
ir.image_resize(file_path, file_name)

print("Hello World -- Python")
