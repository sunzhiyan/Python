# -*- encoding: utf-8 -*-
'''
@File : 9.py
@Time : 2020/04/10 20:35:16
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import os 
import requests
url="https://p.ssl.qhimg.com/t019c8c40312508cdc2.jpg"
d='D:\\'
path=d+url.split('/')[-1]
if not os.path.exists(path) :
    r=requests.get(url)
    r.raise_for_status()
    with open(path,'wb') as f :
        f.write(r.content)
        f.close()
        print("图片保存成功")
else :
    print("图片保存失败或文件已存在")
