#! /usr/bin/env python
# -*- coding=utf-8 -*-

from appium import webdriver
from time import sleep

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4'
desired_caps['deviceName'] = 'c46f2d08'
desired_caps['appPackage'] = 'com.eg.android.AlipayGphone'
desired_caps['appActivity'] = '.AlipayLogin'
# desired_caps['app-wait-activity'] = ''
# desired_caps['unicodeKeyboard'] = True
# desired_caps['resetKeyboard'] = True

try:driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
except:print u"应用打开失败..."
sleep(5)
#id = nearby_layout
try:driver.find_element_by_name(u"咻一咻").click()
except: print u"点击[咻一咻]失败"
sleep(3)
#id = huxi
# 初始化礼包的数量
flag = "6000000"

count = 0
while flag != "0000000":
    #获取剩余的礼包数:className = android.widget.TextView
    count_str = driver.find_elements_by_xpath("//android.widget.TextSwitcher/android.widget.TextView")
    sleep(0.5)
    try: driver.find_element_by_id("huxi").click()
    except Exception,e:flag = "0000000"; print "Error:",e
    count += 1
    # 获取剩余礼包数量
    flag = count_str[0].text + \
           count_str[1].text + \
           count_str[2].text + \
           count_str[3].text + \
           count_str[4].text + \
           count_str[5].text + \
           count_str[6].text
    print u"点击第：", str(count), u"次"
    print u'剩余', flag, u'个礼包'
    sleep(0.5)