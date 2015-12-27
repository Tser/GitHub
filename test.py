#! /usr/bin/env python
# coding=utf-8

import requests

print requests.get("https://github.com/Tser/python/blob/master/Headers/header.json").content
