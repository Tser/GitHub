#! /usr/bin/env python
# coding=utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print s.connect('111.13.101.208')
