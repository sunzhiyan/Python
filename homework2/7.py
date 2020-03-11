# -*- encoding: utf-8 -*-
'''
@File : 7.py
@Time : 2020/03/10 23:36:14
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import random
def num(list2):
    print("生成的随机列表为:",list2)
    for i in range(len(list2)) :
        if list2[i]>=90 :
            print(list2[i],"的等级是A")
        else : 
            if list2[i]>=80 :
                print(list2[i],"的等级是B")
            else :
                if list2[i]>=70 :
                    print(list2[i],"的等级是C")
                else :
                    print(list2[i],"的等级是D")

list2=random.sample(range(1,100),20)
num(list2)