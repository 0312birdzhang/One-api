#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import sys
import urllib2
import datetime
import json
import time
import datetime

url = 'http://v3.wufazhuce.com:8000/api/'

def getHtml(api):
    i_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",\
                 "Referer": 'http://www.wufazhuce.com/'}
    req = urllib2.Request(url+api, headers=i_headers)
    try:
        response = urllib2.urlopen(req,timeout=30)
        allhtml = response.read()
        return allhtml
    except Exception as e:
        print(e)

def gettimedelta(date):
    today = time.strftime("%Y-%m-%d", time.localtime())
    today = datetime.datetime.strptime(today,'%Y-%m-%d')
    thatday = datetime.datetime.strptime(date,'%Y-%m-%d')
    timedelta = (today - thatday).days
    return timedelta
    
    
def queryContent(date):
    
    vindex = gettimedelta(date)
    #home page
    h_api = "hp/idlist/0"
    h_datas = getHtml(h_api)
    h_index = h_datas["data"][vindex]
    h_detail_api = "hp/detail/"+h_index
    h_detail_datas = getHtml(h_detail_api)
    h_data = h_detail_datas.get("data")
    titulo = h_data.get("hp_title")
    imagen = h_data.get("hp_img_url")
    imagen_leyenda =h_data.get("hp_author")
    cita = h_data.get("hp_content")
    cita_content=""
    cita_author=""
    if "by" in cita:
        cita_content = cita.split("by")[0]
        cita_author = "by "+cita.split("by")[1]
    else:
        cita_content = cita.split("from")[0]
        cita_author = "from "+cita.split("from")[1]
    makettime = h_data.get("hp_makettime")
    dom = datetime.datetime.strptime(makettime, '%Y-%m-%d %H:%M:%S').date().strftime("%d")
    may =  datetime.datetime.strptime(makettime, '%Y-%m-%d %H:%M:%S').date().strftime("%B %Y")

    #######other
    o_api = "reading/index/"
    o_datas = getHtml(o_api)
    essay_index = o_datas.get("data").get("essay")[vindex].get("content_id")
    question_index = o_datas.get("data").get("question")[vindex].get("question_id")
    essay_api = "essay/" + essay_index
    essay_datas = getHtml(essay_api).get("data")
    comilla_cerrar = essay_datas.get("guide_word")
    articulo_titulo = essay_datas.get("hp_title")
    articulo_autor = essay_datas.get("hp_author")
    articulo_contenido = essay_datas.get("hp_content")
    articulo_editor = essay_datas.get("hp_author_introduce")
    question_api = "question/"+question_index
    question_datas = getHtml(question_api).get("data")
    cuestion_title = question_datas.get("question_title")
    cuestion_question = question_datas.get("question_content")
    cuestion_answerer = question_datas.get("answer_title")
    cuestion_contenians = question_datas.get("answer_content")
    cosas_imagen = ""
    cosas_titulo = ""
    cosas_contenido = ""
    one_map= {
            "titulo":titulo,
            "imagen":imagen,
            "imagen_leyenda":imagen_leyenda,
            "cita_content":cita_content,
            "cita_author":cita_author,
            "dom":dom,
            "may":may,

            "comilla_cerrar":comilla_cerrar,
            "articulo_titulo":articulo_titulo,
            "articulo_autor":articulo_autor,
            "articulo_contenido":articulo_contenido,
            "articulo_editor":articulo_editor,

            "cuestion_title":cuestion_title,
            "cuestion_question":cuestion_question,
            "cuestion_answerer":cuestion_answerer,
            "cuestion_contenians":cuestion_contenians,

            "cosas_imagen":cosas_imagen,
            "cosas_titulo":cosas_titulo,
            "cosas_contenido":cosas_contenido
        }
    #print(one_map)
    return one_map

    


if __name__ == "__main__":
    queryContent("2016-02-03")
