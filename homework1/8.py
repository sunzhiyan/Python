# -*- encoding: utf-8 -*-
'''
@File : 8.py
@Time : 2020/03/10 20:58:22
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
dict1={'num' : '01', 'name' : 'a', 'workage' : 5, 'salary' : 5000}
dict2={'num' : '02', 'name' : 'b', 'workage' : 7, 'salary' : 7000}
dict3={'num' : '03', 'name' : 'c', 'workage' : 3, 'salary' : 2500}
dict4={'num' : '04', 'name' : 'd', 'workage' : 10, 'salary' : 6000}
dict5={'num' : '05', 'name' : 'e', 'workage' : 8, 'salary' : 6000}
dict6={'num' : '06', 'name' : 'f', 'workage' : 7, 'salary' : 8000}
dict7={'num' : '07', 'name' : 'g', 'workage' : 5, 'salary' : 8000}
dict8={'num' : '08', 'name' : 'h', 'workage' : 2, 'salary' : 9000}
dict9={'num' : '09', 'name' : 'i', 'workage' : 1, 'salary' : 800}
dict10={'num' : '10', 'name' : 'j', 'workage' : 6, 'salary' : 4500}
list1=[dict1,dict2,dict3,dict4,dict5,dict6,dict7,dict8,dict9,dict10]
for i in range(0,10) :
    for j in range(0,10):
        if(list1[i]['salary']<list1[j]['salary']):
            dict=list1[i]
            list1[i]=list1[j]
            list1[j]=dict
for i in range(0,10):
    print(list1[i])