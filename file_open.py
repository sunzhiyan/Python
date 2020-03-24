# -*- encoding: utf-8 -*-
'''
@File : 练习二.py
@Time : 2020/03/24 16:19:56
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import os
import datetime
# 打开指定目录文件
f=open(r'D:\Python\file\a_file\aa.txt','w')
f.write('今天是 ')
f.write(datetime.datetime.now().strftime('%Y-%m-%d'))
f.close()
# 相对路径
os.chdir("file")
with open(r"b_file\a.txt","w") as f :
    f.write('今天是 ')
    f.write(datetime.datetime.now().strftime('%Y-%m-%d'))

os.chdir("a_file")
with open(r"..\b_file\a.txt","r") as f :
    print(f.read())