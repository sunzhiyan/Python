# -*- encoding: utf-8 -*-
'''
@File : 2.py
@Time : 2020/04/27 00:10:09
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import requests
from bs4 import BeautifulSoup
import re
list1=[]
headers = {
    'Host' 'e43cgpmw5dopgeqr.onion'
    'Content-Type'	:'application/x-www-form-urlencoded',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Connection':'keep-alive',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0',
    'Upgrade-Insecure-Requests'	:'1',

    }
with open('web.txt','r') as f :
    i=0
    for lines in f.readlines() :
        if i==100 :
            break
        list1.append(lines.strip('\n'))
        i=i+1

url=list1[4]
r=requests.get(url,headers=headers,verify=False)

soup=BeautifulSoup(r.content,'html.parser')
a=soup.select('a')



for j in range(len(list1)) :
    url=list1[j]
    r=requests.get(url,headers=headers,timeout=30)
    soup=BeautifulSoup(r.content,'html.parser')
    a=soup.select('a')
    for i in a:
        if i.string=="关于我们" or i.string=='企业介绍' or i.string=='企业发展' or i.string=='发展历史' or i.string=='企业概况':
            findb_ur=i['href']
            url1=url+"/"
            url2=url1+findb_ur
            print(url2)



