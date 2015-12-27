#! /usr/bin/env python
# -*- coding: utf-8 -*-

from appium import webdriver
from time import sleep
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4'
desired_caps['deviceName'] = ''
desired_caps['appPackage'] = ''
desired_caps['appActivity'] = ''
# desired_caps['app-wait-activity'] = ''
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
sleep(0.5)
driver.find_element_by_name(u"全部").click()
sleep(1)
driver.find_element_by_id('iv_common_header_right').click()
sleep(1)
word = driver.find_element_by_id('et_search')
word.clear()
word.send_keys(u'中文')
