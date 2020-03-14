# -*- encoding: utf-8 -*-
'''
@File : def_sort.py
@Time : 2020/03/14 22:29:43
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
list1=[('a',88),('b',99),('c',67),('d',77),('e',56),('f',89),('g',55),('h',98),('i',89),('j',86)]
list1.sort(key = lambda x : x[1])
for i in range(len(list1)) :
    print(list1[i])