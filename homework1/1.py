# -*- encoding: utf-8 -*-
'''
@File : 1.py
@Time : 2020/03/10 17:49:20
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
list1= list(range(0, 50))
res=filter(lambda x : x%2!=0,list1)
print("0到50之间的奇数有:")
print(list(res))
res1=filter(lambda x: x%2==0,list1)
print("0到50之间的偶数有:")
print(list(res1))

res2=[]
i=2
for i in range(2,50):
    j=2
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        res2.append(i)
print("0到50之间的质数有:")
print(res2)

res3=filter(lambda x : x%2==0 | x%3==0,list1)
print("0到50之间能同时被2和3整除的有:")
print(list(res3))