# -*- encoding: utf-8 -*-
'''
@File : 6.py
@Time : 2020/03/10 22:58:24
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
def num(n,list1):
    for i in range(n) :
        num=list1[-1]+list1[-2]
        if num<n :
            list1.append(num)
    print(list1)
list1=[0,1]
print("输入n的值：")
n=int(input())
print("菲波那切数列:")
num(n,list1)