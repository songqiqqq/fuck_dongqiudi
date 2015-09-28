# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 16:31:29 2015

@author: asus
"""
#import pycurl
#import StringIO

#dongqiudi_url='http://www.dongqiudi.com/'
#article_url='http://www.dongqiudi.com/article/120059'

#text=StringIO.StringIO()
#c=pycurl.Curl()
#c.setopt(pycurl.URL,article_url)
#c.setopt(pycurl.HTTPHEADER,["User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"])
#c.setopt(pycurl.WRITEFUNCTION, text.write)
#c.setopt(pycurl.FOLLOWLOCATION, 1)
#c.setopt(pycurl.CUSTOMREQUEST,"delete")

#c.perform()

#print text.getvalue()

import requests
import re
import time
from pymouse import PyMouse
import threading

global NUMBER
global OCCUPYORNOT

dongqiudi_url='http://www.dongqiudi.com/'
article_url='http://www.dongqiudi.com/article/117773'

pattern=re.compile('>\d{1,10}\xe8\xaf\x84\xe8\xae\xba</a>')
s=requests.session() 
m=PyMouse()

want_number=str(345-1)
threads=[]
NUMBER=0
OCCUPYORNOT=0

    
def get_the_count(article_url):
    global NUMBER
    global OCCUPYORNOT
    try:
        response=s.get(article_url,timeout=1).content
        NUMBER=pattern.findall(response)[0].split('\xe8')[0][1:]
    except:
        print 'network is run into problem'
    
    if NUMBER==want_number and OCCUPYORNOT==0:
        
        m.click(1338,65)
        OCCUPYORNOT=1
        print 'the exciting number is ',NUMBER,'then i would occupy it!'
        print '''i have occupy it!
        .............
        ...........
        .............
        ..........'''
        OCCUPYORNOT=1
        
    print 'number is ',NUMBER,' occupy_whether is', OCCUPYORNOT



while True:
    t1=threading.Thread(target=get_the_count,args=(article_url,))
    t1.setDaemon(True)
    t1.start()
    time.sleep(0.01)
    
#<a class="comm" href="#share">2027评论</a>
