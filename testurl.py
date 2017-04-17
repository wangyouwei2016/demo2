#!/usr/bin/python  
# -*- coding: utf-8 -*-  
import os,sys
import time
import pycurl
import MySQLdb
def get_table():
    try:
        conn = MySQLdb.connect(host='10.32.145.112', user='root', passwd='bk@321', db="devops",
                               connect_timeout=10, port=int(3306), charset='utf8')
        cur = conn.cursor()

        sql = "select Url from monitor_url_status"

        cur.execute(sql)
        result = cur.fetchall()

        # print result
        # print len(result)
    except MySQLdb.Error, e:
        pass
    except Exception, e1:
        print e1
    # print result
    for u in result:
        url = u[0]
        print url
        c = pycurl.Curl()
        c.setopt(pycurl.URL, url)
        c.setopt(pycurl.CONNECTTIMEOUT, 5)
        c.setopt(pycurl.TIMEOUT, 8)
        c.setopt(pycurl.NOPROGRESS, 1)
        c.setopt(pycurl.FORBID_REUSE, 1)
        c.setopt(pycurl.MAXREDIRS, 1)
        c.setopt(pycurl.DNS_CACHE_TIMEOUT, 30)
        indexfile = open(os.path.dirname(os.path.realpath(__file__)) + "/content.txt", "wb")
        c.setopt(pycurl.WRITEHEADER, indexfile)
        c.setopt(pycurl.WRITEDATA, indexfile)
        try:
            c.perform()
        except Exception, e:
            print "connecion error:" + str(e)
            indexfile.close()
            #c.close()
            # sys.exit()
        NAMELOOKUP_TIME = c.getinfo(c.NAMELOOKUP_TIME)
        CONNECT_TIME = c.getinfo(c.CONNECT_TIME)
        PRETRANSFER_TIME = c.getinfo(c.PRETRANSFER_TIME)
        STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)
        TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
        HTTP_CODE = c.getinfo(c.HTTP_CODE)
        SIZE_DOWNLOAD = c.getinfo(c.SIZE_DOWNLOAD)
        HEADER_SIZE = c.getinfo(c.HEADER_SIZE)
        SPEED_DOWNLOAD = c.getinfo(c.SPEED_DOWNLOAD)

        print "http状态码：%s" % (HTTP_CODE)
        print "DNS解析时间：%.2f ms" % (NAMELOOKUP_TIME * 1000)
        print "建立连接时间：%.2f ms" % (CONNECT_TIME * 1000)
        print "准备传输时间：%.2f ms" % (PRETRANSFER_TIME * 1000)
        print "传输开始时间：%.2f ms" % (STARTTRANSFER_TIME * 1000)
        print "传输结束总时间：%.2f ms" % (TOTAL_TIME * 1000)
        print "http头部大小：%d bytes" % (HEADER_SIZE)
        print "下载数据包大小：%d bytes" % (SIZE_DOWNLOAD)
        print "平均下载速度：%d KB/s" % (SPEED_DOWNLOAD / 1024)


        sql1 = "UPDATE monitor_url_status set HttpCode='%s',DnsTime='%s',ConnectTime='%s',TotalTime='%s',SizeDownload='%s',SpeedDownload='%s' WHERE Url='%s'" %(HTTP_CODE,NAMELOOKUP_TIME*1000,CONNECT_TIME*1000,TOTAL_TIME*1000,SIZE_DOWNLOAD,SPEED_DOWNLOAD,url)

        cur.execute(sql1)
        conn.commit()
    conn.close()

get_table()
# urllist = get_table()
# for url in urllist:
#
#     print url

# def monitor():
#
#     result = get_table('10.32.145.112', 'root', 'bk@321', 3306)
#     print [result]
    # for s in result[3]:
    #     print s

#
#
# urllist = ['www.baidu.com','http://www.sfsfhiwf322.com/','http://www.cnblogs.com/tobeprogramer/p/398243317.html','www.163.com']
#
# for url in urllist:
#     c=pycurl.Curl()
#     c.setopt(pycurl.URL, url)
#     c.setopt(pycurl.CONNECTTIMEOUT, 5)
#     c.setopt(pycurl.TIMEOUT, 8)
#     c.setopt(pycurl.NOPROGRESS, 1)
#     c.setopt(pycurl.FORBID_REUSE,1)
#     c.setopt(pycurl.MAXREDIRS, 1)
#     c.setopt(pycurl.DNS_CACHE_TIMEOUT, 30)
#     indexfile = open(os.path.dirname(os.path.realpath(__file__))+"/content.txt","wb")
#     c.setopt(pycurl.WRITEHEADER, indexfile)
#     c.setopt(pycurl.WRITEDATA,indexfile)
#     try:
#         c.perform()
#     except Exception,e:
#         print "connecion error:"+str(e)
#         # indexfile.close()
#         # c.close()
#         # sys.exit()
#     NAMELOOKUP_TIME = c.getinfo(c.NAMELOOKUP_TIME)
#     CONNECT_TIME = c.getinfo(c.CONNECT_TIME)
#     PRETRANSFER_TIME = c.getinfo(c.PRETRANSFER_TIME)
#     STARTTRANSFER_TIME =c.getinfo(c.STARTTRANSFER_TIME)
#     TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
#     HTTP_CODE = c.getinfo(c.HTTP_CODE)
#     SIZE_DOWNLOAD = c.getinfo(c.SIZE_DOWNLOAD)
#     HEADER_SIZE = c.getinfo(c.HEADER_SIZE)
#     SPEED_DOWNLOAD = c.getinfo(c.SPEED_DOWNLOAD)
#
#     print "http状态码：%s" %(HTTP_CODE)
#     print "DNS解析时间：%.2f ms" %(NAMELOOKUP_TIME*1000)
#     print "建立连接时间：%.2f ms" %(CONNECT_TIME*1000)
#     print "准备传输时间：%.2f ms" %(PRETRANSFER_TIME*1000)
#     print "传输开始时间：%.2f ms" %(STARTTRANSFER_TIME*1000)
#     print "传输结束总时间：%.2f ms" %(TOTAL_TIME*1000)
#     print "http头部大小：%d bytes" %(HEADER_SIZE)
#     print "下载数据包大小：%d bytes" %(SIZE_DOWNLOAD)
#     print "平均下载速度：%d KB/s" %(SPEED_DOWNLOAD/1024)
#
#
#     indexfile.close()
#     c.close()
#
#
