#! /usr/bin/env python
# coding=utf-8

'''
        OS：windows8.1
        python2.7.10
        IDE：pycharm4.5
        node -v = 0.10.26
        npm -v = 1.4.6
        appium：1.4.13.1
        platformName: MI NOTE
        双卡双待...
        Test android call...
        version=0.1
        time：2015.11.5
'''
from appium import webdriver
from time import sleep
caps = {}
caps['platformName'] = 'Android'
caps['platformVersion'] = '4.4'
caps['deviceName'] = ''  # 当前链接设备唯一时，可以为空？        YES
caps['appPackage'] = 'com.android.contacts'
caps['appActivity'] = '.activities.PeopleActivity'
caps['unicodeKeyboard'] = True
caps['resetKeyboard'] = True
callNum = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
           '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '0': 'zero'}
callTo = '11111111111'
try:
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        # 元素属性text值唯一时，可以直接使用name来定位元素
        driver.find_element_by_name(u'拨号').click()
        # driver.find_element_by_name(u'联系人').click()
        # driver.find_element_by_name(u'黄页').click()
        # 元素text值不唯一时，可以通过className的值来定位（定位好className，判断属性值是否为某一特定的值）
        call = driver.find_element_by_class_name('android.widget.Button')
        assert call.get_attribute('text') == u'拨号'
        call.click()
        # driver.find_element_by_id('one').click()        # is OK
        for s in callTo:
                driver.find_element_by_id(callNum[s]).click()
        driver.find_element_by_id('call_sim2')  # 使用卡2拨打电话：
except Exception, e:
        print e.message
finally:
        sleep(5)  # 为了查看结果...
        # 执行此语句，为了结束本次对话(即：session)，方便下次执行脚本不再重新启动appium服务
        driver.quit()
