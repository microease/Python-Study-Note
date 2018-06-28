#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
@Author：joy_nick
@博客：http://byd.dropsec.xyz/
'''

import requests
import sys
f = open('url.txt', 'r')
url = f.readlines()
length = len(url)
url_result_success=[]
url_result_failed=[]
for i in range(0,length):
 try:
 response = requests.get(url[i].strip(), verify=False, allow_redirects=True, timeout=5)
 if response.status_code != 200:
 raise requests.RequestException(u"Status code error: {}".format(response.status_code))
 except requests.RequestException as e:
 url_result_failed.append(url[i])
 continue
 url_result_success.append(url[i])
f.close()
result_len = len(url_result_success)
for i in range(0,result_len):
 print '网址%s' % url_result_success[i].strip()+'打开成功'