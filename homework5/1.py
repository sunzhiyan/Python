# -*- encoding: utf-8 -*-
'''
@File : 1.py
@Time : 2020/04/18 21:13:17
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import time,random
def outer(func):
    def inner() :
        start_time=time.time()
        func()
        end_time=time.time()
        print("运行时间为:%s"%(end_time-start_time))
    return inner
def index():
    time.sleep(random.randrange(1,5))
    print("welcome")
index=outer(index)
index()