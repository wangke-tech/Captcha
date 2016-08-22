#!/usr/bin/env python
# encoding: utf-8

import os
from PIL import Image

dir = '../pic/'
path = '../font/'


def binarization(image):
    """ 二值化处理。
    二值化是图像分割的一种常用方法。在二值化图像的时候，把大于临界灰度值的像素灰度设置为灰度极大值，把小于这个灰度临界值的像素灰度设置为灰度极小值。根据阈值选取的不同，二值化算法分为自适应阈值和固定阈值，这里我们采用较为简单的固定阈值。
    把像素点大于阈值的设置为1，小于阈值的设置为0,生成一张查找表，再用point进行映射。"""

    threshold = 140
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    imgbin = image.point(table, '1')
    return imgbin


def deversion(image):
    for i in range(4):
        x = 16 + i * 15
        y = 2
        return image.crop((x, y, x +7, y +10))

if '__main__' == __name__:
    for f in os.listdir(dir):
        if f.endswith('.gif'):
            im = Image.open(dir + f)

            # 第一步: 把彩色图像转化为灰度图像，RGB转化为HSL彩色空间，采用L分量
            imgry = im.convert('L')

            # 第二步: 二值化处理
            imgbin = binarization(imgry)

            imgbin.save(path +f)

            # 第三步: 图片切割
            deversion(imgbin).show()


