#! /usr/bin/env python
# coding=utf-8
from selenium import webdriver
import time

web = webdriver.Chrome()
web.get("http://mail.163.com")
web.maximize_window()
web.find_element_by_id("idInput").send_keys("自己的账号")
web.find_element_by_id("pwdInput").send_keys("自己的密码")
time.sleep(1)
web.find_element_by_id("loginBtn").click()

time.sleep(3)
web.find_element_by_css_selector("b.nui-ico.fn-bg.ga0").click()
web.find_element_by_css_selector(".nui-editableAddr-ipt").send_keys("目标邮箱")
web.find_element_by_css_selector(".nui-ipt-input[maxlength='256']").send_keys("主题内容")
frame = web.find_element_by_css_selector(".APP-editor-iframe")
web.switch_to_frame(frame)
web.find_element_by_css_selector(".nui-scroll").send_keys("发送的邮件正文")
web.switch_to_default_content()
web.find_element_by_css_selector("b.nui-ico-sent").click()
