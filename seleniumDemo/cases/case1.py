#! /usr/bin/env python
# coding=utf-8

from selenium import webdriver
from time import sleep


class siteTest:
    def __init__(self, url, userName, passWd):
        self.url = url
        self.name = userName
        self.passwd = passWd
        self.browser = webdriver.Chrome()
        pass

    def login(self):
        self.browser.get(self.url)
        self.browser.maximize_window()
        sleep(2)
        inputName = self.browser.find_element_by_id("idInput")
        # inputName = self.browser.find_element_by_name("username")
        # inputName = self.browser.find_element_by_link_text()
        # inputName = self.browser.find_element_by_class_name("formIpt")
        # inputName = self.browser.find_element_by_css_selector("input#idInput")
        sleep(2)
        inputName.clear()
        inputName.send_keys(self.name)
        inputPasswd = self.browser.find_element_by_id("pwdInput")
        sleep(2)
        inputPasswd.clear()
        inputPasswd.send_keys(self.passwd)
        sleep(1)
        login = self.browser.find_element_by_id("loginBtn").click()
        try:
            err = self.browser.find_element_by_css_selector("div.error-tt > p")
            return err.get_attribute("text")

        except Exception, e:
            return "pass"
        finally:
            self.browser.quit()
