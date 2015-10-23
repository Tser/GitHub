#! /usr/bin/env python
# coding=utf-8
'''
    selenium 用python写脚本的最大好处就是语言简洁，需要些的代码量也是比较少
                        本脚本是为了模仿百度搜索功能
'''
from selenium import webdriver
# 目标url
dec_url = 'http://www.baidu.com'
# 打开chrome浏览器
bs = webdriver.Chrome()
# 再浏览器中打开网址
bs.get(dec_url)
# 锁定操作的目标
kw = bs.find_element_by_id('kw')
kw.clear()
kw.send_keys(u'selenium')
submit = bs.find_element_by_id('su')
submit.click()
