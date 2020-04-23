# -*- encoding: utf-8 -*-
'''
@File : 4.py
@Time : 2020/04/21 23:04:45
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
class student :
    name=''
    age=0
    sex=''
    English=0
    Math=0
    Chinese=0
    def __init__(self,n,a,s,e,m,c) :
        self.name=n
        self.age=a
        self.sex=s
        self.English=e
        self.Math=m
        self.Chinese=c
        self.__sum()
    def __sum(self) :
        sum=self.English+self.Math+self.Chinese
        ave=sum/3
        print("姓名：",self.name,"年龄:",self.age,"性别:",self.sex,"总分:",sum,"平均分:",ave)
stu=student('a',18,'女',77,88,89)
