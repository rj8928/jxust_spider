# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
from lxml import etree
from scrapy.selector import Selector
import json
import time
header ={
        "Referer": "http://jw.jxust.edu.cn/tjkbcx.aspx?xh=20141927&xm=%C8%D9%BF%A1&gnmkdm=N121601",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
"Connection":"keep-alive"
                    }
def kebiao():
    sess = requests.session()
    sess.headers = header
    cookie = {"ASP.NET_SessionId":"rfbqyx452e4dan55mz4gzu55"}
    requests.utils.add_dict_to_cookiejar(sess.cookies,cookie)
    url = 'http://jw.jxust.edu.cn/tjkbcx.aspx?xh=20141927&xm=%C8%D9%BF%A1&gnmkdm=N121601'
    response = sess.get(url,headers = header).text
    # print response
    response = etree.HTML(response)
    __VIEWSTATE = response.xpath("//input[@name='__VIEWSTATE']/@value")[0]
    # print 'xueyuan'
    # print __VIEWSTATE
    xn =['2012-2013', '2013-2014', '2014-2015', '2015-2016','2016-2017']
    xq = ['1', '2']
    nj = ['2012', '2013', '2014' ,'2015' ,'2016']
    xy = [['01', '资源与环境工程学院'], ['02', '建筑与测绘工程学院'], ['04', '机电工程学院'], ['05', '信息工程学院'], ['06', '经济管理学院'], ['07', '文法学院'], ['08', '外语外贸学院'], ['09', '理学院'], ['10', '冶金与化学工程学院'], ['11', '材料科学与工程学院'],
          ['12', '电气工程与自动化学院']]

    for xuenian in xn:
        for xueqi in xq:
            for nianji in nj:
                for xueyuan,xueyuanname in xy:

                    form = {
                    "__EVENTTARGET": "xy",
                    "__EVENTARGUMENT":"",
                    "__VIEWSTATE":__VIEWSTATE,
                    "xn":xuenian,
                    "xq":xueqi,
                    "nj":nianji,
                    "xy":xueyuan,
                    "zy":"",
                    "kb":""
                    }

                    response = sess.post(url, data=form).text
                    response = etree.HTML(response)
                    __VIEWSTATE = response.xpath("//input[@name='__VIEWSTATE']/@value")[0]
                    # print 'zhuanye'
                    # print __VIEWSTATE
                    zhuanye = response.xpath("//select[@name='zy']/option/@value")
                    zhuanyename = response.xpath("//select[@name='zy']/option/text()")
                    # print zhuanyename
                    # print 8888888
                    # print zhuanye
                    while '' in zhuanyename:
                        zhuanyename.remove('')
                    while '' in zhuanye:
                        zhuanye.remove('')
                    zhuanyelist = []
                    for i in range(len(zhuanye)):
                        list = []
                        list.append(zhuanye[i])
                        list.append(zhuanyename[i])
                        zhuanyelist.append(list)
                    # print zhuanye
                    for zhuanye,zhuanyename in zhuanyelist:
                        form = {
                            "__EVENTTARGET": "zy",
                            "__EVENTARGUMENT": "",
                            "__VIEWSTATE": __VIEWSTATE,
                            "xn": xuenian,
                            "xq": xueqi,
                            "nj": nianji,
                            "xy": xueyuan,
                            "zy": zhuanye,
                            "kb":"",
                        }
                        response = sess.post(url, data=form).text
                        a = sess.headers
                        # print a
                        # print 9999
                        # print response
                        response = Selector(text=response)
                        __VIEWSTATE = response.xpath("//input[@name='__VIEWSTATE']/@value").extract()
                        # print __VIEWSTATE
                        # print 'kebiao'
                        banji = response.xpath("//select[@name='kb']/option/@value").extract()

                        banjiname = response.xpath("//select[@name='kb']/option/text()").extract()
                        # print banji
                        while '' in banjiname:
                            banjiname.remove('')

                        while '' in banji:
                            banji.remove('')
                        # print banji
                        if len(banji)==0:
                            print '课表为空,下一个班级'
                            continue
                        banjilist = []
                        for i in range(len(banji)):
                            list = []
                            list.append(banji[i])
                            list.append(banjiname[i])
                            banjilist.append(list)

                        for banji,banjiname in banjilist:
                            form = {
                                "__EVENTTARGET": "kb",
                                "__EVENTARGUMENT": "",
                                "__VIEWSTATE": __VIEWSTATE,
                                "xn": xuenian,
                                "xq": xueqi,
                                "nj": nianji,
                                "xy": xueyuan,
                                "zy": zhuanye,
                                "kb": banji
                            }
                            response = sess.post(url, data=form).text
                            response = Selector(text=response)
                            __VIEWSTATE = response.xpath("//input[@name='__VIEWSTATE']/@value").extract()[0]
                            coursetable = response.xpath('//table[@id="Table6"]//td[@rowspan="2"]')
                            # for course in coursetable:
                            #     course = course.split('<br>')
                            #     print 88888
                            #     print course
                            #     print 99999
                            #     if len(course)>
                            # print coursetable
                            courses = {"xuenian": xuenian,
                                       "xueqi": xueqi,
                                       "nianji": nianji,
                                       "xueyuanname": xueyuanname,
                                       "zhuanyename": zhuanyename,
                                       "banjiname": banjiname,
                                       "coursetable": banji}
                            print courses

                            courses = json.dumps(courses, ensure_ascii=False) + '\n'
                            with open('calss2.json', 'a') as f:
                                f.write(courses.encode('utf-8'))
                            for courseinfo in coursetable:

                                courseinfo = courseinfo.xpath("./text()").extract()
                                if len(courseinfo) < 3:
                                    continue
                                courses = {"coursetable":banji,
                                           "course":courseinfo[0],
                                           "teacher":courseinfo[2]}
                                print courses
                                courses = json.dumps(courses,ensure_ascii=False) + '\n'
                                with open('course2.json','a') as f:
                                    f.write(courses.encode('utf-8'))
                            # print courses

                            coursetable2 = response.xpath('//table[@id="DataGrid1"]//tr')

                            for coursetable2 in coursetable2[1:]:
                                courseinfo = coursetable2.xpath("./td/text()").extract()
                                courses = {"coursetable":banji,
                                           "course": courseinfo[0],
                                           "teacher": courseinfo[1]}
                                courses = json.dumps(courses,ensure_ascii=False) + '\n'
                                with open('course2.json','a') as f:

                                    f.write(courses.encode('utf-8'))
                            print 'sleep 2s'
                            time.sleep(2)



kebiao()
