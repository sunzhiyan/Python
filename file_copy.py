# -*- encoding: utf-8 -*-
'''
@File : file_copy.py
@Time : 2020/03/25 08:41:39
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
path1=r'D:\Python\test.txt'
path2=r'D:\Python\file\test.txt'
def copy(path1,path2) :
    try:
        with open(path1,"r") as f :
            with open(path2,"w") as fi:
                fi.write(f.read())
    except IOError:
        print("File is not accessible.")
copy(path1,path2)