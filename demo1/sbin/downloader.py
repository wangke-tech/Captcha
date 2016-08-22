#!/usr/bin/env python
# encoding: utf-8
"""
下载验证码
"""
import urllib
PIC_NUM = 50   # 图片下载数量
URL = 'https://passport.csdn.net/ajax/verifyhandler.ashx'   # 验证码地址


def download(url, pic_num):
    for i in range(PIC_NUM):
        print 'download', i
        file('../pic/%04d.gif' %i, 'wb').write(urllib.urlopen(url).read())

if '__main__' == __name__:
    download(URL, PIC_NUM)
