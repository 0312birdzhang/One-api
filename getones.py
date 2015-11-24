#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年10月13日

@author: 0312birdzhang
'''
import sqlite3
import json
from htmlparse import queryContent 
def getTodayContent(vol):
    try:
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS datas
                 (vol int, json text) ''')
        cur.execute('SELECT json FROM datas WHERE vol= %s ' % vol)
        result= cur.fetchone()
        #logging.debug(result)
        if result:
            return json.dumps(json.loads(result[0]),ensure_ascii=False,indent=2)
        else:
            data=queryContent(vol)
            #插入
            if data and data != "Timeout":
                insertDatas(vol,data)
                return json.dumps(data,ensure_ascii=False,indent=2)
            else:
                return 'Error'
    except Exception as e:
        return 'Error'
    conn.close()

#插入数据
def insertDatas(vol,data):
    try:
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO datas VALUES (%s,'%s')" % (vol,json.dumps(data) ) )
        conn.commit()
    except Exception as e:
        #pass
     conn.close()





