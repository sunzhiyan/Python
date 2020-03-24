# -*- encoding: utf-8 -*-
'''
@File : 练习.py
@Time : 2020/03/18 08:21:30
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import os
pwd = os.path.abspath('.')
print(pwd)
print( os.path.basename('/python/hello.py') )   # 返回文件名
print( os.path.dirname('/python/hello.py') )    # 返回目录路径
print( os.path.split('/python/hello.py') )      # 分割文件名与路径
print( os.path.join('python','test','hello.py') )  # 将目录和文件名合成一个路径
