#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年10月14日

@author: 0312birdzhang
'''
import web
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
        return "欢迎使用一个API，接口实例： http://one.birdzhang.xyz/query?vol=1111"

class query:
    def GET(self):
        web.header('Content-Type', 'application/json')
        i = web.input()
        return getTodayContent(i.vol)
    
if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
