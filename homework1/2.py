# -*- encoding: utf-8 -*-
'''
@File : 2.py
@Time : 2020/03/10 18:08:06
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
dict={ '01' : 92, '02' : 86, '03' : 56, '04' : 86, '05' : 99, '06' : 88, '07' : 77, '08' : 42, '09' : 79, '10' : 100}
for i in dict:
    if(dict[i]>80):
        print(list(dict.keys())[list(dict.values()).index(dict[i])],':',dict[i])
