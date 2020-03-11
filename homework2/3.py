# -*- encoding: utf-8 -*-
'''
@File : 3.py
@Time : 2020/03/10 22:41:53
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import random
def sum(list2):
    list2=random.sample(range(1,20),10)
    print("随机列表为:")
    print(list2)
    print("列表中的奇数为:")
    for i in range(0,len(list2)):
        if(list2[i]%2!=0):
            print(list2[i])
list2=[]
sum(list2)