# -*- encoding: utf-8 -*-
'''
@File : 3.py
@Time : 2020/04/18 23:10:58
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
list1=[{'key' : '123','value' : '123'},{'key' : '456','value' : '456'},{'key' : '789','value' : '789'}]
def login(func) :
    def inner() :
        log=0
        username=input("输入用户名：")
        for line in list1 :
            if line['key']==username :
                log=1
                password=input("输入密码:")
                if line['value']==password :
                    print("登录")
                    func()
                    break;
                else :
                    print("密码错误!")
        if log==0 :
            print("账户不存在")
    return inner
@login
def func() :
    print("执行函数")
func()
