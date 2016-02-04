#! /usr/bin/env python
# -*- coding=utf-8 -*-

'''
    Android手机的计算器应用
'''

from appium import webdriver
from time import sleep


desired_caps = {}
desired_caps['platformName'] = 'Android'                                #系统的名称
desired_caps['platformVersion'] = '4.4'                                 #系统的版本号
desired_caps['deviceName'] = 'c46f2d08'                                 #设备的名称（设备号）
desired_caps['appPackage'] = 'com.android.calculator2'                  #应用的包名
desired_caps['appActivity'] = '.Calculator'                             #应用的入口
# desired_caps['app-wait-activity'] = ''
# desired_caps['unicodeKeyboard'] = True                                #安装appium输入法
# desired_caps['resetKeyboard'] = True                                  #设置输入法

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps) #调用appium服务端的服务

driver.find_element_by_id(u'清除').click()
driver.find_element_by_name('7').click()
sleep(0.5)
driver.find_element_by_name(u'减').click()
sleep(0.5)
driver.find_element_by_name('6').click()
sleep(0.5)
driver.find_element_by_name(u'等于').click()
# driver.quit()