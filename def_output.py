# -*- encoding: utf-8 -*-
'''
@File : def_output.py
@Time : 2020/03/07 11:30:24
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

lis1= list(range(0, 20))
res=filter(lambda x: x%2!=0,lis1)
print(list(res))