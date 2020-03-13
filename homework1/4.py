# -*- encoding: utf-8 -*-
'''
@File : 4.py
@Time : 2020/03/10 19:55:27
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
a=int(input("请输入年份:"))
if((a%4==0 and a%100!=0) or (a%400==0)):
    print(a,"年为闰年")
else :
    print(a,"年不是闰年")