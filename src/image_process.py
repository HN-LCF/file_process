# -*- coding: utf-8 -*-
"""
@File       :image_process.py
@Time       :2021/3/23 21:34
@Author     :HN-LCF
@Email      :lou666888out@163.com
@Software   :PyCharm
"""

# todo:
#   -


from PIL import Image


def image_process(fileName):
    """

    :param fileName:
    :return:
    """

    image = Image.open(fileName)  # 读取图片rgb 格式<class 'numpy.array'>
    image = image.resize((2048, 1536))
    image.save('../data/photos/lcf-1.jpg', quality=95, dpi=(30.0, 30.0))  # 调整图像的分辨率为300,dpi可以更改


if __name__ == "__main__":
    file_name = '../data/photos/lcf.jpg'
    image_process(file_name)
