#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年10月13日

@author: 0312birdzhang
'''
import sqlite3
import json
from htmlparse import queryContent 
def getTodayContent(day):
    try:
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS datas
                 (day text, json text) ''')
        cur.execute('SELECT json FROM datas WHERE day= %s ' % day)
        result= cur.fetchone()
        #logging.debug(result)
        if result:
            return json.dumps(json.loads(result[0]),ensure_ascii=False,indent=2)
        else:
            data=queryContent(day)
            #插入
            if data and data != "Timeout":
                insertDatas(day,data)
                return json.dumps(data,ensure_ascii=False,indent=2)
            else:
                return 'Error'
    except Exception as e:
        return 'Error'
    conn.close()

#插入数据
def insertDatas(day,data):
    try:
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO datas VALUES (%s,'%s')" % (day,json.dumps(data) ) )
        conn.commit()
    except Exception as e:
        #pass
     conn.close()





