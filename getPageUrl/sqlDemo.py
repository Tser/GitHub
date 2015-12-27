#! /usr/bin/env python
# coding=utf-8
import sqlite3

sql = sqlite3.connect('a_href.db')
cur = sql.cursor()
# cur.execute('select * from baidu')
cur.executescript('sql3.sql')
sql.commit()
print cur.fetchone()
cur.close()
sql.close()
