# -*- encoding: utf-8 -*-
'''
@File : 9.py
@Time : 2020/03/11 22:33:12
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
def paixu(list1) :
    list2=[]
    for i in range(len(list1)) :
        for j in range(len(list1)) :
            if list1[i]<list1[j] :
                num=list1[i]
                list1[i]=list1[j]
                list1[j]=num
    print(list1)
print("以列表的形式输入一组数：")
list=eval(input())
paixu(list)