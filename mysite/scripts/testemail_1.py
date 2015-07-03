#!/usr/bin/env python
# -*- coding:utf-8 -*-
import smtplib
smtp = smtplib.SMTP()   
smtp.connect("smtp.126.com", "25")   
smtp.login('cuimiracle', 'nsjjfz639781')  
tolist = ["cuimiracle@126.com"] 
msg = '''\\
From: Me@my.org
To:cuimiracle@126.com;cuimiracle@gmail.com
Subject: testin

This is a test '''
smtp.sendmail('cuimiracle@126.com', tolist, msg)   
smtp.quit() 