#! /usr/bin/env python
# coding=utf-8
import re, requests, urllib2

test_url = {
    "baidu": 'http://www.baidu.com',
    "qq": "http://www.qq.com",
    "sina": "http://sina.com"
}
with open("proxy.txt") as f:
    proxy = f.readlines()
for p in proxy:
    proxies = {
        'http': 'http://' + re.match('\d+\.\d+\.\d+\.\d+:\d+', str(p)).group(0),
        'https': 'https://' + re.match('\d+\.\d+\.\d+\.\d+:\d+', str(p)).group(0)
    }
    # for url in test_url:
    try:
        code = requests.get(test_url['baidu'], proxies=proxies, timeout=10).status_code
        if code == 200:
            open("ip_data.txt", 'a').write(re.match('\d+\.\d+\.\d+\.\d+:\d+', str(p)).group(0) + '\n')
            print 'Proxy:', p , test_url['baidu'], 'is OK'
        else:
            print 'Proxy:', p , test_url['baidu'], 'code:', code
    except:
        print 'Proxy:', p , test_url['baidu'], "connect Error"
        pass
