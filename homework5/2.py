# -*- encoding: utf-8 -*-
'''
@File : 2.py
@Time : 2020/04/18 21:18:49
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
def log(func):
    def inner():
        f=open("日志.txt","a")
        f.write("执行"+func.__name__+'\n')
        f.close()
        ret=func()
        return ret
    return inner
@log
def func_1():
    print("执行一次func_1")
@log
def func_2():
    print("执行一次func_2")
func_1()
func_1()
func_2()
func_2()