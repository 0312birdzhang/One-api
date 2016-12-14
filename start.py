#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年10月14日

@author: 0312birdzhang
'''
from gevent import monkey; monkey.patch_all()  
from gevent.wsgi import WSGIServer  
import gevent
import web
import time
from getones import *
import sys,os 
reload(sys)
sys.setdefaultencoding('utf8')
urls = (
    '/', 'index',
    '/query', 'query'
)
class index:
    def GET(self):
        return "欢迎使用一个API，接口实例： http://one.birdzhang.xyz/query?day=2016-02-01"

class query:
    def GET(self):
        web.header('Content-Type', 'application/json')
        today = time.strftime("%Y-%m-%d", time.localtime())
        i = web.input(day=today)
        return getTodayContent(i.day,today)
 
def getTodayVol():
       #new Date("2012-10-07 00:00:00").getTime();
       start = "2012-10-07 00:00:00"
       timeArray = time.strptime(start, "%Y-%m-%d %H:%M:%S")
       timeStamp = int(time.mktime(timeArray))
       today = int(time.time())
       vol = (today - timeStamp)/60/60/24
       return vol
if __name__ == "__main__":
    application = web.application(urls, globals()).wsgifunc()
    WSGIServer(('', 9998), application).serve_forever()
