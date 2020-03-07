# -*- encoding: utf-8 -*-
'''
@File : def_id.py
@Time : 2020/03/07 11:27:37
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

def ChangeInt( a ):
    print("a重新赋值之前的地址:",id(a))
    a.append([4,5,10])
    print("a重新赋值后的值:",a)
    print("a重新赋值后的地址:",id(a))
 
b = [5,6,7,8,9]
print('b的地址:',id(b))
ChangeInt(b)
print('传了参数后的b的地址:',id(b))
print('b的值:', b )
