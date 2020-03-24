# -*- encoding: utf-8 -*-
'''
@File : file_read1.py
@Time : 2020/03/24 19:38:09
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import os
list1=[]
list2=[]
with open('file_read.txt','r',encoding='utf8') as f:
    for line in f.readlines() :
        list1.append(line.split())
for i in range(len(list1)) :
    if i>0 :
        list1[i][2]=int(list1[i][2])
for i in range(len(list1)) :
    for j in range(len(list1)) :
        if i>0 and j>i :
            if list1[i][2]>list1[j][2] :
                list=list1[i]
                list1[i]=list1[j]
                list1[j]=list   
for i in range(len(list1)) :
    if i>0 :
        list1[i][2]=str(list1[i][2]) 
fi=open("file_read1.txt","w")
for i in range(len(list1)) :
    s=' '.join(list1[i])
    fi.write(s)
    fi.write('\n')
fi.close()
with open('file_read1.txt','r') as fil :
    for line in fil.readlines() :
        print(line.strip())