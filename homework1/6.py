# -*- encoding: utf-8 -*-
'''
@File : 6.py
@Time : 2020/03/10 20:27:59
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
list1=[0,1]

for i in range(100) :
    num=list1[-1]+list1[-2]
    if num<100 :
        list1.append(num)
print(list1)