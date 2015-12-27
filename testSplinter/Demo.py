#! /usr/bin/env python
# coding=utf-8

import requests
from urlparse import urlparse
import urllib, urllib2
from ghost import Ghost


class searchData:
    def __init__(self, keyword):
        self.ghost = Ghost()
        self.kw = urllib.quote(keyword)
        self.site = {
            'td': 'https://s.taobao.com/search?&q=',  # 淘宝
            'jd': 'http://search.jd.com/Search?keyword=',  # 京东
            'yd': 'http://search.yhd.com/c0-0/k',  # 一号店
            'yx': 'http://searchex.yixun.com/html?key=u',  # 易迅
            'lf': 'http://search.lefeng.com/search/noresult?keyWord=',  # 乐蜂网
            'an': 'http://www.amazon.cn/s/ref=nb_sb_noss_1/475-4397139-2107651?field-keywords=',  # 亚马逊
            'vl': 'http://s.vancl.com/search?k=',  # 凡客诚品
            'ge': 'http://search.gome.com.cn/search?question=',  # 国美在线
            'sg': 'http://search.suning.com/'  # 苏宁易购
        }
        self.list = ['td', 'jd', 'yx', 'lf', 'an', 'vl', 'ge', 'sg']

        for s in self.list:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) '
                              'AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/43.0.2357.132 Safari/537.36',
                'Referer': urlparse(self.site[s]).scheme + '://' + urlparse(self.site[s]).netloc,
                'Host': urlparse(self.site[s]).netloc
            }
            # print s, len(requests.get(self.site[s], headers=headers).content)
            if s == 'yx':
                # result = requests.get(self.site[s], headers=headers)
                with self.ghost.start() as session:
                    session.open(self.site[s], headers=headers)
                    page, resources = session.wait_for_page_loaded()
                print repr(page.content)


if __name__ == "__main__":
    searchData('数据恢复').KW_result()
'''
td 275415
jd 20163
yd 45620    *
yx 30694    *
lf 19439    *
an 526748
vl 113290   *
ge 43325    *
sg 9579     *
'''
