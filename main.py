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

from src import image_process as ip

print("Start:\n")
file_path = './data/photos/'
file_name = 'lcf.jpg'
ip.image_process(file_path, file_name)

print("Hello World -- Python")
