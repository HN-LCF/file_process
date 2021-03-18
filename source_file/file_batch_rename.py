# -*- coding: utf-8 -*-
"""
@File       :file_batch_rename.py
@Time       :2021/3/18 22:01
@Author     :HN-LCF
@Email      :lou666888out@163.com
@Software   :PyCharm
"""

# todo:
#   -


import os
import sys


def rename():
    path = input("请输入路径(例如D:\\\\picture)：")
    # name = input("请输入开头名:")
    # startNumber = input("请输入开始数:")
    file_type = input("请输入后缀名（如 .jpg、.txt等等）:")
    # print("正在生成以" + name + file_type + "迭代的文件名")
    count = 0
    file_list = os.listdir(path)

    # 输出为 test
    for files in file_list:
        old_file = os.path.join(path, files)
        old_name = os.path.basename(old_file)
        old_name = old_name.split('.')[0]
        print(old_name)
        if os.path.isdir(old_file):
            continue
        new_file = os.path.join(path, '附件1：2019级材料成型及控制工程专业3班'+old_name+'教育评议表'+file_type)
        os.rename(old_file, new_file)
        count += 1
    print("一共修改了" + str(count) + "个文件")


if __name__ == "__main__":
    rename()
