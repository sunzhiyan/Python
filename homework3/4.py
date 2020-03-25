# -*- encoding: utf-8 -*-
'''
@File : 4.py
@Time : 2020/03/24 23:27:23
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import os
os.mkdir("img")
def create_files():
    for i in range(10):
        os.mkdir('img/'+str(i)+'.png')
create_files()
def change(dirname,old_suffix,new_suffix) :
    pngfile = filter(lambda filename : filename.endswith(old_suffix),os.listdir(dirname))
    basefile=[os.path.splitext(filename)[0] for filename in pngfile]
    for filename in basefile :
        oldname = os.path.join(dirname,filename +old_suffix)
        newname = os.path.join(dirname,filename +new_suffix)
        os.rename(oldname,newname)
        print('%s重命名为%s成功' %(oldname,newname))
change('img','.png','.jpg')