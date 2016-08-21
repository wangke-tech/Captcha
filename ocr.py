#!/usr/bin/env python
# encoding: utf-8

import time
#from urllib2.Request import urlretrieve
import subprocess
from selenium import webdriver


# 创建新的Selenium driver
driver = webdriver.PhantomJS(executable_path='<Path to Phantom JS>')
# 有时我发现PhantomJS查找元素有问题，但是Firefox没有
# 如果你运行程序有问题，去掉下面这行注释。
# 用Selenium试试Firefox浏览器：
driver = webdriver.Firefox()

driver.get('http://www.amazon.com/War-Peace-Leon-Nikolayevich-Tolstoy/dp/142703200')
time.sleep(2)

# 单击图书预览按钮
driver.find_element_by_id('sitbLogoImg').click()
imageList = set()

# 等待页面加载完成
time.sleep(5)
# 当向右箭头可以点击时，开始翻页
while "pointer" in driver.find_element_by_id('sitReaderRightPageTurner').get_attribute('style'):
    driver.find_element_by_id('sitbReaderRightPageTruner').click()
    time.sleep(2)
    # 获取宜家在的新页面(一次可以加载多个页面，但是重复的页面不能加到集合中)
    pages = driver.find_element_by_xpath("//div[@class='pageImage']/div/img")
    for page in pages:
        iamge = page.get_attributes('src')
        imageList.add(iamge)
driver.quit()

# 用tesseract处理我们收集的url链接
for image in sorted(imageList):
    urlretrieve(image,'page.jpg')
    imageList.add(image)
    p = subprocess.Popen(['tesseract','page.jpg','page'],stdout=subprocess.PIPE,sederr=subprocess.PIPE)
    p.wait()
    f = open('page.txt','r')
    print f.read()
