# -*- encoding: utf-8 -*-
'''
@File : file_pickle.py
@Time : 2020/03/24 20:21:56
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import pickle
dict1={'num' : '01','name' :'a','age' : 18}
dict2={'num' : '02','name' :'b','age' : 20}
dict3={'num' : '03','name' :'c','age' : 19}
dict4={'num' : '04','name' :'d','age' : 15}
dict5={'num' : '05','name' :'e','age' : 17}
list=[dict1,dict2,dict3,dict4,dict5]
f=open("file_pickle.txt","w")
for i in range(len(list)) :
    s=str(list[i])
    pickle.dump(s,f)
f.close()