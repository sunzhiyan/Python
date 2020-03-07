# -*- encoding: utf-8 -*-
# -*- encoding: utf-8 -*-
'''
@File : 1.13-04.py
@Time : 2020/03/06 09:42:24
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
def myfun(x,*args):
    print('第一个参数:', x)
    print('第二个参数:', args)
    for i in args:
        print('第二个参数里面的值:',i)
    print("输出列表：")
    print(list(args))
    print("输出字典：")
    print(dict(zip(list(args),list(args))))

myfun(11,22,33,44,55)

myfun(11,'a','b','c',55)
