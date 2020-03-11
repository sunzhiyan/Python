# -*- encoding: utf-8 -*-
'''
@File : 10.py
@Time : 2020/03/10 23:26:05
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
def cacluate(x,y) :
    print("两数之和是:",x+y)
    print("两数之差是:",x-y)
    print("两数之积是:",x*y)
    if y!=0:
        print("两数相除是:",x/y)
    else:
        print("除数不能为零")
print("输入要计算的两个数:")
x=int(input())
y=int(input())
cacluate(x,y)