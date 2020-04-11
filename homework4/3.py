# -*- encoding: utf-8 -*-
'''
@File : 3.py
@Time : 2020/04/06 23:26:35
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import base64
import sys
import json
user_list=[]
while True:
    username=input("请用户输入姓名【输入Q或q时退出】：")
    if username.lower()=='q' :
        print("退出")
        break
    else :
        dict={}
        dict['username']=username
        name=input("输入用户账户名：")
        dict['name']=name 
        password=input("输入用户密码：")
        password=password.encode('utf-8')
        bs64=base64.b64encode(password)
        pwd=str(bs64,encoding='utf-8')
        dict['password']=pwd
        user_list.append(dict)
try :
    f=open("user.txt",'w')
    for i in range(len(user_list)) :
        f.write(user_list[i]['username']+'  '+user_list[i]['name']+'    '+user_list[i]['password']+'\n')
    f.close()
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
print("存入文件user.txt中")
