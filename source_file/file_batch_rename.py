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


def file_rename():
    path = input("请输入路径(例如D:\\\\picture)：")
    # name = input("请输入开头名:")
    # startNumber = input("请输入开始数:")
    file_type = input("请输入后缀名（如 .jpg、.txt等等）:")
    # print("正在生成以" + name + file_type + "迭代的文件名")
    count = 0
    file_list = os.listdir(path)

    # 输出为 test
    for files in file_list:
        old_file = os.path.join(path, files)  # 文件路径
        old_name = os.path.basename(old_file)  # 文件全名（带后缀）
        old_name = old_name.split('.')[0]  # 文件全名（无后缀）
        print(old_name)
        if os.path.isdir(old_file):
            continue
        new_file = os.path.join(path, '附件1：2019级材料成型及控制工程专业3班' + old_name + '教育评议表' + file_type)  # 文件新名（带后缀）
        os.rename(old_file, new_file)  # 重命名
        count += 1  # 计数
    print("一共修改了" + str(count) + "个文件")


if __name__ == "__main__":
    file_rename()
