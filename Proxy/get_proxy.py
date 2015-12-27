#! /usr/bin/env python
# coding=utf-8

from ghost import Ghost
# import stackless

ghost = Ghost()

with ghost.start() as session:
    page, resources = session.open("http://jeanphix.me")
