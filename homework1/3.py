# -*- encoding: utf-8 -*-
'''
@File : 3.py
@Time : 2020/03/10 19:49:08
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
print("两个列表相同元素有:")
list1=[12,23,45,56,78,89,98,1,2]
list2=[1,2,3,4,5,6,66,56,9]
for x in list1 :
    for y in list2 :
        if(x==y):
            print(x)