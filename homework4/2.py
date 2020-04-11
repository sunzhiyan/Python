# -*- encoding: utf-8 -*-
'''
@File : 2.py
@Time : 2020/04/06 21:53:14
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import datetime
def time(year,mouth,day,mouth_list) :
    month_days=0
    if year==2020 :
        for j in range(mouth-1):
            month_days=mouth_list[j]+month_days
    else :
        print("输入时间不在本校历计算范围内")
    total_days=month_days+day
    return total_days  
def caculate(num) :
    begin=time(2020,2,16,mouth_list)
    end=time(2020,8,24,mouth_list)
    if num>begin and num<end :
        if (num-begin)%7==0 :
            xingqi=7
            zhou=int((num-begin)/7)
            print("按校历计算第",zhou,"周，周",xingqi)
        else :
            xingqi = (num-begin)%7
            zhou=int((num-begin)/7+1)
            print("按校历计算第",zhou,"周，周",xingqi)
list1=input("请输入你要计算的日期（20200406）")
year=int(list1[:4])
month=int(list1[4:6])
day=int(list1[-2:])
mouth_list=[31,29,31,30,31,30,31,31,30,31,30,31]
a=time(year,month,day,mouth_list)
caculate(a)
