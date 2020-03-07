# -*- encoding: utf-8 -*-
'''
@File : range.py
@Time : 2020/03/04 09:15:44
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
num=list(range(10))
for i in num:
    print(i)
print("偶数为")
for i in num:
    if(i%2==0):
        print(i)
print("完成")