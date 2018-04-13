#!/usr/bin/env python3
# -*- coding:utf8 -*-

import mysql.connector

conn=mysql.connector.connect(user='root', password='68582188',database='awesome')
cursor=conn.cursor()
cursor.execute('select * from users')
data=cursor.fetchall()
print(data)