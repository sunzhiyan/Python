# -*- encoding: utf-8 -*-
'''
@File : 4.py
@Time : 2020/05/05 19:08:03
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode
import os
import time
import random

url = "https://www.programcreek.com/python/"

# 求搜索request的URL
def reque(url) :
    data = {
        "ClassName" : "request",
        "sumit" : "Search"
    }
    time.sleep(random.random()*20)
    request = urlencode(data)
    web_request=url+"?"+request
    return web_request

# 求request检索结果
def requ(url1) :
    list_url=[]
    # list_url1=[]
    headers={}
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/61.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
        ]
    headers['User-Agent'] = random.choice(user_agent_list)
    
    # 新建文件夹request文件放入
    folder=os.path.exists("D:\\Python\\request")
    if not folder :
        os.makedirs("D:\\Python\\request")

    url=reque(url1)
    response=requests.get(url,headers)
    text=response.content.decode('utf-8','ignore')
    soup=BeautifulSoup(text,'html.parser')
    ids=soup.find('ul',id='api-list')
    lis=ids.find_all('li')
    time.sleep(random.random()*20)

    for li in lis :

        time.sleep(random.random()*10)

        a=li.find('a')
        href=a['href']
        list_url.append(href)
        print(a.string)

        # list_url 存放request下所有的URL
        # list_url所对应的的文件夹save_URL 
        save_url="D:\\Python\\request\\"+a.string.replace("\n","")
        folder1=os.path.exists(save_url)
        if not folder1 :
            os.makedirs(save_url)

        # 获取save_url方法的URL
        response1=requests.get(href,headers,timeout=30)
        if response1.status_code==200:
                    pass
        else :
            time.sleep(random.random()*1000)
            print("2222")
            response1=requests.get(href,headers,timeout=100)
        text1=response1.content.decode('utf-8','ignore')
        soup1=BeautifulSoup(text1,'html.parser')
        ids1=soup1.find('ul',id='api-list')
        lis1=ids1.find_all('li')
        time.sleep(random.random()*10)

        for li1 in lis1 :

            time.sleep(random.random()*10)

            a1=li1.find('a')
            href1=a1['href']
            print(a1.string)

            # list_url1存放save——URL下所有方法的URL
            # list_url1.append(href1)
            save_url1=save_url.replace(" ","")

            # 写入以方法名为文件名的txt文件中
            file_path=os.path.join(save_url1,a1.string.replace("\n",""))
            with open(file_path+".txt",'a',encoding = 'gb18030') as fd :

                time.sleep(random.random()*10)

                response_example=requests.get(href1,headers,timeout=100)
                if response_example.status_code==200:
                    pass
                else :
                    time.sleep(random.random()*1000)
                    print('333')
                    response_example=requests.get(href1,headers,timeout=100)
                

                text_example=response_example.content.decode('utf_8','ignore')
                soup_example=BeautifulSoup(text_example,'html.parser')
                ids_example=soup_example.find_all('div',style="margin:20px 2px; color:#424345; font-weight:bold;")
                ids_example1=soup_example.find_all('div',class_="exampleboxbody")
                # ids_example2=ids_example1.find_all('pre',class_="prettyprint")
                for ids_examples,ids_example1s in zip(ids_example,ids_example1) :

                    time.sleep(random.random()*3)
                    
                    ids_example2=ids_example1s.find('pre',class_="prettyprint")
                    fd.write(ids_examples.string)
                    fd.write('\n')
                    if ids_example2.string :    
                        fd.write(ids_example2.string)
                    else :
                        pass
                    fd.write('\n')
                pass
            time.sleep(random.random()*20)
            

def main() :
    url = "https://www.programcreek.com/python/"
    requ(url)

if __name__=='__main__' :
    main()