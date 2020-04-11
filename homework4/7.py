# -*- encoding: utf-8 -*-
'''
@File : 7.py
@Time : 2020/04/08 00:04:23
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import os
ret =os.getcwd()
name = os.path.basename(ret)
sum = 0
def func(dirpath):
    lst = os.listdir(dirpath)  # 大文件夹下文件列表,包括文件夹
    for el in lst:
        new_dir = dirpath+'\\'+el
        if os.path.isfile(new_dir):
            getsize = os.path.getsize(new_dir)
            global sum
            sum += getsize
        else:
            func(new_dir)
    return sum

num = func(ret)
print('文件夹%s的大小为%s字节' % (name,num))