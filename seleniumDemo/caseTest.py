#! /usr/bin/env python
# coding=utf-8

from cases.case1 import siteTest
import unittest
from HTMLTestRunner import HTMLTestRunner


class scriptTest(unittest.TestCase):
    def setUp(self):
        self.url = "http://mail.163.com"

    def tearDown(self):
        pass

    def test_case1(self):
        site = siteTest(self.url, userName="", passWd="")
        self.assertEqual(site.login(), "pass")


if __name__ == '__main__':
    testsuite = unittest.TestSuite()
    testsuite.addTest(scriptTest("test_case1"))
    testsuite.addTest(scriptTest("test_case1"))
    run = HTMLTestRunner(file("result.html", 'wb'), title=u"测试报告", description=u"测试结果：")
    run.run(testsuite)
