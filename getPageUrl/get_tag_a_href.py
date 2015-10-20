#! /usr/bin/env python
# -*- coding: utf-8 -*-


import requests, os, sqlite3, urlparse
from pyquery import PyQuery as pq

class getHref:
    def __init__(self, url='', mode='get', headers=None, data=None):
        if os.path.exists('a_href.db') is False:
            open('a_href.db', 'w')
        self.url = url
        self.mode = mode
        self.headers = headers
        self.data = data
        self.scheme = urlparse.urlparse(self.url).scheme     #协议名
        self.netloc = urlparse.urlparse(self.url).netloc     #域  名
        self.html = None
        self.page_tag_a_href = []
        if self.headers is None:
            self.headers = {
                      'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/43.0.2357.132 Safari/537.36',
                      'Referer': self.scheme + '://' + self.netloc,
                      'Host': self.netloc
            }
    def get_page(self):
        if self.scheme == 'http':
            if self.mode == 'get':
                self.html = requests.get(self.url, headers=self.headers).content
            elif self.mode =='post':
                self.html = requests.post(self.url, data=self.data, headers=self.headers).content
            else:
                print u'目前只支持GET 与 POST'
                self.html = None
        else:
            if self.mode == 'get':
                self.html = requests.get(self.url, headers=self.headers, verify=False).content
            elif self.mode =='post':
                self.html = requests.post(self.url, data=self.data, headers=self.headers, verify=False).content
            else:
                print u'目前只支持GET 与 POST'
    def get_a_href(self):
        # getHref(self.url).get_page()
        if self.html:
            for a in pq(self.html).find('a'):
                href = pq(a).attr('href')
                if href != None:
                    if href.find('javascript') == -1:
                        if urlparse.urlparse(href).netloc == '':
                            self.page_tag_a_href.append(self.scheme + '://' + self.netloc + href)
                        else:
                            self.page_tag_a_href.append(href)
        list(set(self.page_tag_a_href))        #去重
        # map(getHref(self.url).write_sql, self.page_tag_a_href)
        # def write_sql(self, URL):
        table_name = self.netloc.split('.')[-2]
        sql_ser = sqlite3.connect('a_href.db')
        # sql_ser.isolation_level = None          #自动提交
        sql_cu = sql_ser.cursor()
        # 判断是否已存在表
        sql_cu.execute('select count(*) from sqlite_master where type="table" and name="' + table_name + '"')
        reslut_table_status = sql_cu.fetchone()
        if reslut_table_status[0] == 0:
            # 创建表
            sql_cu.execute('create table ' +
                           table_name +
                           ' (id integer primary key, netloc varchar(50), url varchar(128), status varchar(10))')
            print table_name, u'表以创建'
        else:
            print table_name, u'表已存在'
        for URL in self.page_tag_a_href:
            print URL
            sql_cu.execute("insert into '%s'(netloc, url, status) values('%s', '%s', 'OK')" % (table_name, urlparse.urlparse(URL).netloc, URL))
            sql_ser.commit()
            print sql_cu.fetchone()              #获取执行后的结果
        sql_cu.close()
        sql_ser.close()
        print 'write sql end'

if __name__ == "__main__":
    gg = getHref('http://www.dianping.com/search/category/1/10/g110')
    gg.get_page()
    gg.get_a_href()