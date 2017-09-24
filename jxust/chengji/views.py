# coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
import getcode
import requests
from lxml import etree
from scrapy.selector import Selector
import re
# Create your views here.
header ={
        "Referer": "http://jw.jxust.edu.cn/xs_main.aspx?xh=20141927",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"
                    }



def index(request):
    cookiedict,_VIEWSTATE = getcode.code()
    imagename = cookiedict['ASP.NET_SessionId']
    request.session['cookie'] = cookiedict
    request.session['_VIEWSTATE'] = _VIEWSTATE

    return render(request,'jxust.html',{'imagename':imagename})

def showcode(request, username, password):
    cookie = getcode.code()
    request.session['cookie'] = cookie

def loginhandle(request):
    cookiedict = request.session.get('cookie')
    _VIEWSTATE = request.session.get('_VIEWSTATE')
    username = request.POST.get('userid')
    request.session['userid'] = username
    password = request.POST.get('pwd')
    code = request.POST.get('code')
    url = "http://jw.jxust.edu.cn/default2.aspx/"
    form = {
        "__VIEWSTATE": _VIEWSTATE,
        "txtUserName": username,
        "TextBox2": password,
        "txtSecretCode": code,
        "RadioButtonList1": "学生",
        "Button1": "",
        "lbLanguage": "",
        "hidPdrs": "",
        "hidsc": "",
    }
    sess = requests.session()
    # 每次都带
    requests.utils.add_dict_to_cookiejar(sess.cookies, cookiedict)
    # 只带这一次
    response = sess.post(url, data=form, headers=header)
    # cookiejar = sess.cookies
    # 8. 将CookieJar转为字典：
    # cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
    # print cookiedict
    if response.url.find('main.aspx') != -1:
        red = HttpResponseRedirect('/result/')
        return red
    else:
        return HttpResponse("账号密码或验证码错误")


def showchengji(request):

    cookiedict = request.session.get('cookie')
    userid = request.session.get('userid')
    header = {
        "Referer": "http://jw.jxust.edu.cn/xs_main.aspx?xh=" + str(userid),
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36"
    }
    print 9999
    print cookiedict
    sess = requests.session()
    # 每次都带
    requests.utils.add_dict_to_cookiejar(sess.cookies, cookiedict)
    # response = response.text
    # # print response
    # response = etree.HTML(response)
    # _VIEWSTATE = response.xpath("//form/input[3]/@value")[0]
    # print _VIEWSTATE
    url2 = "http://jw.jxust.edu.cn/xscj_gc.aspx?xh=" + str(userid)+"&xm=%C8%D9%BF%A1&gnmkdm=N121605"

    # print 888
    # print cookiedict
    # print 999
    response=sess.get(url2, headers = header).text
    print response
    response = etree.HTML(response)
    print response
    try:
        _VIEWSTATE = response.xpath("//form/input/@value")[0]
    except Exception as e:
        return HttpResponseRedirect('/')
    # print _VIEWSTATE
    form = {
        "__VIEWSTATE": _VIEWSTATE,
        "ddlXN": "",
        "ddlXQ": "",
        "Button2": "在校学习成绩查询"
    }
    response = sess.post(url2, data = form, headers=header).text
    # response = etree.HTML(response)
    table = Selector(text=response)
    info = table.xpath('string(//p[@class="search_con"])').extract()[0]
    a = info.find('学年'.decode('utf-8'))
    info2 = table.xpath('string(//select[@id="ddlXN"])').extract()[0]
    print info2
    info2 =  info2.strip().replace('\t','').splitlines()

    info = info[:a]
    # print info
    # print info2
    table = table.xpath('//table[@id="Datagrid1"]')

    xuenian = table.xpath('.//td[1]/text()').extract()
    xueqi = table.xpath('.//td[2]/text()').extract()
    kechengdaima = table.xpath('.//td[3]/text()').extract()
    kechengmingcheng = table.xpath('.//td[4]/text()').extract()
    kechengxinzhi = table.xpath('.//td[5]/text()').extract()
    xuefen = table.xpath('.//td[7]/text()').extract()
    jidian = table.xpath('.//td[8]/text()').extract()
    chengji = table.xpath('.//td[9]/text()').extract()
    # fuxiubiaoji = table.xpath('//td[10]/text()').extract()
    bukaochengji = table.xpath('.//td[11]/text()').extract()
    chongxiuchengji = table.xpath('.//td[12]/text()').extract()
    xueyuanmingcheng = table.xpath('.//td[13]/text()').extract()
    num = len(xuenian)
    # print str(num) + '9999999999'
    list = [xuenian,xueqi,kechengdaima,kechengmingcheng,kechengxinzhi,xuefen,jidian,chengji,bukaochengji,chongxiuchengji,xueyuanmingcheng]
    context = []
    for i in range(num):
        list2 = []
        for j in list:
            list2.append(j[i])
        # print list2
        context.append(list2)

    # context = {
    #     'xuenian':xuenian, 'xueqi':xueqi, 'kechengdaima':kechengdaima,'kechengmingcheng':kechengmingcheng, 'kechengxinzhi':kechengxinzhi, 'xuefen':xuefen,
    #     'jidian':jidian, 'chengji':chengji, 'bukaochengji':bukaochengji,
    #     'chongxiuchengji':chongxiuchengji, 'xueyuanmingcheng':xueyuanmingcheng,
    #     'num':num
    # }
    return render(request, 'result.html', {'content':context , 'info':info, 'info2':info2})



