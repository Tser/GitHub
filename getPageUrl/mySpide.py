#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests, re, time, urllib2


class mySpide:
    def __init__(self, baseURL):
        self.baseURL = baseURL  # 存放基础网址
        self.allURL = []  # 存放抓取的所有url
        self.cacheURL = []
        self.allURL.append(self.baseURL)
        self.cacheURL.append(self.baseURL)

    # 【提取有用的数据】对URL—Page页内的URL进行提取：
    # 经过筛选的URL写入到allURL和cacheURL中：
    def doData(self):
        URL1 = []
        URL2 = []
        URL3 = []
        try:
            if len(self.cacheURL[0]) != 0:
                url = self.cacheURL[0]
                # print url
            else:
                print u"结束！"
                return -1
        except:
            return u"已结束"
        try:
            content = requests.get(url).content
            # 备用
            # content = urllib2.urlopen(url).read()
            time.sleep(0.5)
        except:
            print url, u"链接超时"
            self.cacheURL.pop(0)
            pass
        try:
            URL1 = re.findall("<a[^>]+>", content)
            # 在在每个a标签中提取出href的字符串
            for url in URL1:
                URL2.append(re.findall("href=\"[^\"]+\"", url))
            # 提取url字符串
            for ur in URL2:
                try:
                    if (ur[0].split("\""))[1].find("javascript") == -1:
                        URL3.append((ur[0].split("\""))[1])
                except:
                    pass
            # url字符串处理
            for u in URL3:
                if u[0] != 'h' and u[0] != '/':
                    u = self.baseURL + '/' + u
                if u[0] != 'h' and u[0] == '/':
                    u = self.baseURL + u
                # 添加到allURL中的做限制：必须是之前未保存过的，只存储一个域名中的url
                try:
                    ###############################需要重新构造######################################
                    x = u.split(".")
                    for mx in x:
                        if (mx.find((self.baseURL).split(".")[-2]) != -1) and (u not in self.allURL):
                            self.allURL.append(u)
                            self.cacheURL.append(u)
                except:
                    pass
            # 去除第一个元素
            self.cacheURL.pop(0)
        except:
            pass


if __name__ == "__main__":
    doMain = "http://yqkapp.sinaapp.com/"
    # doMain = "http://www.line0.com/"
    # doMain = "http://www.dianping.com"
    if doMain[-1] == '/':
        doMain = doMain[:-1]
    start = mySpide(doMain)
    startTime = time.time()
    while 1:
        if start.doData() == u"已结束":
            # print start.allURL
            print u"\n共有：" + \
                  str(len(start.allURL)) + \
                  u"个" + \
                  u"\n共用时：" + \
                  str(time.time() - startTime) + \
                  '(s)'
            break

# 使用urllib2
# 共有：72个
# 共用时：67.6550002098(s)

# 使用requests
# 共有：72个
# 共用时：70.856000185(s)
