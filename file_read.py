# -*- encoding: utf-8 -*-
'''
@File : file_read.py
@Time : 2020/03/24 17:29:47
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import os
with open('file_read.txt','r',encoding='utf8') as f :
    for line in f.readlines() :
        print(line.strip())