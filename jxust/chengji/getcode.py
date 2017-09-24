# coding=utf-8

import requests
from lxml import etree

header ={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"
                    }

def code():
    url = 'http://jw.jxust.edu.cn/'
    url1 = 'http://jw.jxust.edu.cn/CheckCode.aspx/'
    sess = requests.session()
    html = sess.get(url,headers = header).text
    html = etree.HTML(html)
    _VIEWSTATE = html.xpath("//form/input/@value")[0]
    print _VIEWSTATE
    # codedata = sess.get(url1, headers = header).content
    cookiejar = sess.cookies
    # 8. 将CookieJar转为字典：
    cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
    print cookiedict
    sessionid = cookiedict['ASP.NET_SessionId']
    codedata = sess.get(url1, headers=header).content
    with open('static/code/' + sessionid + '.gif', 'wb') as f:
        f.write(codedata)
    return cookiedict,_VIEWSTATE
