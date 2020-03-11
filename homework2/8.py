# -*- encoding: utf-8 -*-
'''
@File : 8.py
@Time : 2020/03/11 07:47:17
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
def search(str,dict) :
    num=0
    for i in range(len(str)) :
        if str[i] in dict.keys() :
            dict[str[i]]=dict[str[i]]+1
        else :
            dict.update({str[i] : 1})
    print("每个字母的个数为:")
    print(dict)
    for value in dict.values() :
        if value>num :
            num=value
    print("出现次数最高的字母为:")
    for key,value in dict.items() :
        if value==num :
            print(key)
print("输入字符串:")
str=input()
dict={}
search(str,dict)
