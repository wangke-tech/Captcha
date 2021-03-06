#!/usr/bin/env python
# encoding: utf-8

from urllib import urlretrieve
from urllib2 import urlopen
from bs4 import BeautifulSoup
import subprocess
import requests
from PIL import Image
from PIL import ImageOps


def cleanImage(imagePath):
    image = Image.open(imagePath)
    image = image.point(lambda x: 0 if x < 143 else 255)
    borderImage = ImageOps.expand(image,border=20,fill='white')
    borderImage.save(imagePath)

html = urlopen('http://www.pythonscraping.com/humans-only').read()
bsObj = BeautifulSoup(html)
# 收集需要处理的表单数据
imageLocation = bsObj.find('img',{'title':'Image CAPTCHA'})['src']
fromBuildId = bsObj.find('input',{'name':'form_build_id'})['value']
captchaSid = bsObj.find('input',{'name':'captcha_sid'})['value']
captchaToken = bsObj.find('input',{'name':'captcha_token'})['value']

captchaUrl = 'http://pythonscraping.com' + imageLocation
urlretrieve(captchaUrl,"captcha.jpg")
cleanImage('captcha.jpg')

p = subprocess.Popen(['tesseract','captcha.jpg','captcha'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
p.wait()
f = open('captcha.txt','r')

# 清理识别结果中的空格和换行符
captchaResponse = f.read().replace(' ','').replace('\n','')
print 'captcha solution attempt: ' + captchaResponse

if len(captchaResponse) == 5:
    params = {'captcha_token': captchaToken, 'captcha_sid':captchaSid,'captcha_response':captchaResponse,'name':'Ryan Mitchell','subject':'I come to seek the Grail','comment_body[und][0][value]':'...and I am definitedly not a bot'}

    r = requests.post('http://www.pythonscraping.com/comment/reply/10',data=params)
    responseObj = BeautifulSoup(r.text)
    if responseObj.find('div',{'class':'messages'}) is not None:
        print responseObj.find('div',{'class':'messages'}).get_text()
else:
    print 'There is a problem reading the CAPTCHA correctly!'
