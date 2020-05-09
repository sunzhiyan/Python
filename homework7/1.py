# -*- encoding: utf-8 -*-
'''
@File : 1.py
@Time : 2020/04/25 23:49:24
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import re
list1=[]
with open('webspiderUrl.txt','r',encoding='utf_8') as f :
    with open('web.txt','a') as f1:
        i=0
        for lines in f.readlines() :
            list1.append(lines.strip())
        for i in range(10000) :
            li=re.findall(r'http://[0-9a-zA-Z_.-]{0,40}',list1[i],re.M|re.I)
            for j in range(len(li)) :
                f1.write(li[j]+'\n')                 
    print("保存如文件web.txt中")

            
