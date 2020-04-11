# -*- encoding: utf-8 -*-
'''
@File : 6.py
@Time : 2020/04/07 22:20:24
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import os
import time
def file1(file_dir) :
    dir_list=os.listdir(file_dir)
    list_file=[]
    for i in range(len(dir_list)) :
        list1=[]
        list1.append(dir_list[i])
        mtime=time.ctime(os.path.getmtime(dir_list[i]))
        list1.append(mtime)
        if os.path.isfile(dir_list[i]) :
            str='文件'
            list1.append(str)
            filesize=os.path.getsize(dir_list[i])
            filesize=filesize/float(1024*1024)
            list1.append(filesize)
        else :
            str='文件夹'
            list1.append(str)
        list_file.append(list1)
    for i in range(len(list_file)) :
        for j in range(len(list_file[i])) :
            print(list_file[i][j],end='  ')
        print()
file_dir=os.getcwd()
file1(file_dir)