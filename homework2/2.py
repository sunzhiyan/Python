# -*- encoding: utf-8 -*-
'''
@File : 2.py
@Time : 2020/03/10 22:22:05
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
def sum(list2,num):
    print("输入要加和的数字:")
    list1=input().split()
    for i in range(0,len(list1)) :
        list2.append(int(list1[i]))
    for i in range(0,len(list2)) :
        num=num+list2[i]
    print(num)
list2=[]
num=0
sum(list2,num)
