#! /usr/bin/env python
# -*- coding=utf-8 -*-
'''
    尝试 知乎
'''
import requests as req
from urlparse import urlparse
from pyquery import PyQuery as pq
import json, time, os, sys

class zhihu:
    def __init__(self):
        self.HOME_URL = 'http://www.zhihu.com'
        self.TOPICS_URL = 'http://www.zhihu.com/topics'
        self.DAILY_URL = 'http://daily.zhihu.com'
        self.HEADERS = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip,deflate,sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Host': urlparse(self.HOME_URL).netloc,
            'Referer': urlparse(self.HOME_URL).netloc,
            'User-Agent': 'Chrome/36.0.1941.0 Safari/537.36'
        }
        pass

    def get_topics_data(self):
        topics_lists = {} #存放大类数据信息
        data = {'title': '', 'url': ''}
        self.HEADERS['Host'] = urlparse(self.TOPICS_URL).netloc
        topics_page = req.get(self.TOPICS_URL, headers=self.HEADERS).content
        #获取大类话题  go-->
        a_lists = pq(topics_page)('ul.zm-topic-cat-main > li > a')
        for n in range(len(a_lists)):
            data['title'] = pq(a_lists[n]).text()
            data['url'] = self.TOPICS_URL + pq(a_lists[n]).attr('href')
            topics_lists.keys().append(pq(a_lists[n]).text())
            topics_lists[pq(a_lists[n]).text()] = data
        return topics_lists
    # @get_topics_data
    def get_topics_childs_data(self):
        #child-node定位：div.zh-general-list
        pass
    def get_top_new_data(self):
        page_1 = req.get(self.URL, headers=self.HEADERS).content
        titles = pq(page_1)('div.content > h2 > a')
        count = pq(page_1)('div.content > div.entry-body  > div.zm-item-vote > a')
        for n in range(len(titles)):
            print u'TOP标题',str(n+1)+':', pq(titles[n]).text(),'\t', u'热度:', pq(count[n]).attr('data-votecount')
            if urlparse(pq(titles[n]).attr('href')).netloc:
                print 'URL:', pq(titles[n]).attr('href')
            else:
                print 'URL:', self.HOME_URL + pq(titles[n]).attr('href')
    #知乎日报的图和标题
    def get_daily_data(self):
        daily = {} #收集日报数据
        self.HEADERS['Host'] = urlparse(self.DAILY_URL).netloc
        daily_page = req.get(self.DAILY_URL, headers=self.HEADERS).content
        daily_all_tag_a = pq(daily_page)('a.link-button')
        for n in range(len(daily_all_tag_a)):
            data = {'title': '', 'url': '', 'image': ''} #重复使用data字典，需要初始化，清除内部的信息
            data['title'] = pq(daily_all_tag_a[n])('span').text()
            data['url'] = self.DAILY_URL + pq(daily_all_tag_a[n]).attr('href')
            data['image'] = pq(daily_all_tag_a[n])('img').attr('src')
            daily[n] = data
        #下载知乎日报首页的相册
        #========download images==============
        try:
            if False == os.path.exists(time.strftime('%Y%m%d')):
                os.mkdir(time.strftime('%Y%m%d'))
        except:pass
        finally:
            for n in range(len(daily_all_tag_a)):
                # print n, type(n)
                image_url = daily[n]['image']
                image_file = time.strftime('%Y%m%d') + '/' + image_url.split('/')[-1]
                _image = req.get(image_url, stream=True)
                image_size = _image.headers['Content-Length']
                if 200 == _image.status_code:
                    with open(image_file, 'wb') as f:
                        for chunk in _image.iter_content(chunk_size=1024):
                            if chunk:
                                f.write(chunk)
                                sys.stdout.write(str(len(chunk)*100/int(image_size)) + '%')
                                sys.stdout.flush()
                                f.flush()
            print 'images download finis!'
        return daily
if __name__ == '__main__':
    #查看知乎话题标题:zhihu().get_topics_data().keys()[0]|[-1]
    # 知乎-话题-互联网-精华
    # url = 'http://www.zhihu.com/topic/19550517/top-answers'
    # print zhihu().get_topics_data().keys()
    print zhihu().get_daily_data()