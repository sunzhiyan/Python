# -*- encoding: utf-8 -*-
'''
@File : 3.py
@Time : 2020/03/24 22:58:23
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
list1=[]
try :
    with open("student.txt","r",encoding='utf8') as f :
        for line in f.readlines() :
            list1.append(line.split())
    for i in range(len(list1)) :
        if i>0 :
            list1[i][2]=int(list1[i][2])
    for i in range(len(list1)) :
        for j in range(len(list1)) :
            if i>0 and j>i :
                if list1[i][2]<list1[j][2] :
                    list=list1[i]
                    list1[i]=list1[j]
                    list1[j]=list
    for i in range(len(list1)):
        print(list1[i][0]+'   '+list1[i][1]+'   '+str(list1[i][2]))
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])