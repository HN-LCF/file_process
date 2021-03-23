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


import cv2

from PIL import Image


def image_process(file_name):
    """

    :param file_name:
    :return:
    """

    img = cv2.imread(file_name)  # 读取图片rgb 格式<class 'numpy.ndarray'>
    image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))  # 格式转换，bgr转rgb
    image = image.resize((206, 283))
    image.save('./data/photos/wjm-1.jpg', quality=95, dpi=(30.0, 30.0))  # 调整图像的分辨率为300,dpi可以更改


if __name__ == "__main__":
    file_name = './data/photos/wjm.jpg'
    image_process(file_name)