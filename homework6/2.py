# -*- encoding: utf-8 -*-
'''
@File : 2.py
@Time : 2020/04/20 23:24:05
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
class student :
    name=''
    age=0
    score_China=0
    score_Math=0
    score_English=0
    def __init__(self,n,a,w1,w2,w3) :
        self.name=n
        self.age=a
        self.score_China=w1
        self.score_Math=w2
        self.score_English=w3
    def get_name(self) :
        return self.name
    def get_age(self) :
        return self.age
    def get_course(self) :
        max=0
        if self.score_China>max :
            max=self.score_China
        if self.score_Math>max :
            max=self.score_Math
        if self.score_English>max :
            max=self.score_English
        return max
stu1=student('a',18,99,89,90)
print("姓名",stu1.get_name(),"年龄",stu1.get_age(),"最高分",stu1.get_course())
stu2=student('b',18,100,99,87)
print("姓名",stu2.get_name(),"年龄",stu2.get_age(),"最高分",stu2.get_course())

