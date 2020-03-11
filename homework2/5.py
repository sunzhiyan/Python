# -*- encoding: utf-8 -*-
'''
@File : 5.py
@Time : 2020/03/11 21:36:16
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
def diction(dict) :
    for key,value in dict.items() :
        if len(value)>2 :
            value=value[0:2]
            dict.update({key : value})
    print("返回的字典为:")
    print(dict)
print("请输入字典:")
dict=eval(input())
diction(dict)