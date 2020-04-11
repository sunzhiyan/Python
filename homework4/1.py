# -*- encoding: utf-8 -*-
'''
@File : 1.py
@Time : 2020/04/06 21:20:30
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
from collections import deque
import datetime
q=deque([1,2,3,4,5,6,7,8,9,10])
a=datetime.datetime.now()
q.appendleft(11)
b=datetime.datetime.now()
print("尾插所用时间为:",b-a)
c=datetime.datetime.now()
q.append(12)
d=datetime.datetime.now()
print("头插所用时间为:",d-c)
print(q)