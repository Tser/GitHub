#! /usr/bin/env python
# coding=utf-8

import unittest
from appium import webdriver
from time import sleep


class myBigTest(unittest.TestCase):
    def setUp(self):
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
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)

    def testCase1(self):
        try:
            # 元素属性text值唯一时，可以直接使用name来定位元素
            self.driver.find_element_by_name(u'拨号').click()
            # driver.find_element_by_name(u'联系人').click()
            # driver.find_element_by_name(u'黄页').click()
            # 元素text值不唯一时，可以通过className的值来定位（定位好className，判断属性值是否为某一特定的值）
            call = self.driver.find_element_by_class_name('android.widget.Button')
            assert call.get_attribute('text') == u'拨号'
            call.click()
            # driver.find_element_by_id('one').click()        # is OK
            for s in self.callTo:
                self.driver.find_element_by_id(self.callNum[s]).click()
            self.driver.find_element_by_id('call_sim2')  # 使用卡2拨打电话：
        except Exception, e:
            print e.message

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
