# -*- encoding: utf-8 -*-
'''
@File : 8.py
@Time : 2020/04/09 22:16:39
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import random
ip=['172.25.254.'+str(i) for i in range(0,225)]
with open('ip.txt','w') as f :
    for count in range(1200) :
        f.write(random.sample(ip,1)[0]+'\n')
def paixu(file) :
    ip_dict=dict()
    with open (file) as f :
        for ip in f :
            if ip in ip_dict :
                ip_dict[ip]+=1
            else :
                ip_dict[ip]=1
    sorted_ip=sorted(ip_dict.items(),key=lambda x : x[1],reverse=True)[:10]
    for i in range(10) :
        print(sorted_ip[i][0])
paixu('ip.txt')