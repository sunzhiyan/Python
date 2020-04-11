# -*- encoding: utf-8 -*-
'''
@File : 4.py
@Time : 2020/04/07 17:18:09
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import base64
import sys
import json
list1=[]
try :
    with open("user.txt","r") as f :
        for line in f.readlines() :
            list1.append(line.split())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
def denglu() :
    username=input("请输入用户姓名:")
    name=input("请输入账号")
    password=input("请输入密码:")
    num=0
    for i in range(len(list1)) :
        if list1[i][0]==username :
            if name==list1[i][1] :
                bs6=bytes(list1[i][2],encoding='utf-8')
                bs=base64.b64decode(bs6)
                pwd=str(bs,encoding='utf-8')
                if pwd==password :
                    num=1
                    print("登陆成功")
                    break
    if num==0 :
        print("登录失败")
            
denglu()

