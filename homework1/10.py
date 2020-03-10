# -*- encoding: utf-8 -*-
'''
@File : 10.py
@Time : 2020/03/10 21:32:17
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
str='it is very good it is beautiful i like it very mach'
list1=str.split()
dict={}
for x in list1 :
    if x in dict.keys() :
        dict[x]=dict[x]+1
    else :
        dict.update({x : 1})
print(dict)