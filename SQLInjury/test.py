#! /usr/bin/env python
# coding=utf-8

import requests, json, time

sqlmapURL = "http://127.0.0.1:8775"
# 首先申请一个taskid
taskURL = sqlmapURL + "/task/new"
r = requests.get(taskURL)
sessionID = r.json()['taskid']
print u"已经申请taskid：", sessionID
time.sleep(2)

# 发送扫描数据,开始扫描
targetURL = ""
scanURL = sqlmapURL + "/scan/" + sessionID + "/start"
data = json.dumps({'url': targetURL})
header = {'Content-type': 'application/json'}
requests.post(scanURL, data, header, timeout=25)
print targetURL, u"已扫描完..."
time.sleep(2)

# 查看状态
statusURL = sqlmapURL + "/scan/" + sessionID + "/status"
dataURL = sqlmapURL + "/scan/" + sessionID + "/data"
statusJSON = requests.get(statusURL).json()['success']
print u"状态已查看：",
if statusJSON:
    print u"扫描已完成..."
    print requests.get(dataURL, timeout=5).json()
