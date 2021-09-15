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


def image_resize(path, name):
    """
    Modify the size of image.

    :param path: path of image file to be modified.
    :param name: name of image file to be modified.
    :return: Generate a new image named `new_img.jpg` in the `path`.
    """

    image = Image.open(path + name)  # 读取图片rgb 格式<class 'numpy.array'>
    image = image.resize((2048, 1536))
    image.save(path + 'new_img.jpg', quality=95,
               dpi=(30.0, 30.0))  # 调整图像的分辨率为300,dpi可以更改


if __name__ == "__main__":
    file_path = '../data/photos/'
    file_name = 'lcf.jpg'
    image_resize(file_path, file_name)
