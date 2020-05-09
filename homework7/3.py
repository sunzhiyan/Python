# -*- encoding: utf-8 -*-
'''
@File : 3.py
@Time : 2020/05/05 18:54:21
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import quote
import os
import sys

def mp3(url) :
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
    response=requests.get(url,headers)
    text=response.content.decode('utf_8','ignore')
    soup=BeautifulSoup(text,'html.parser')
    ids=soup.find('div',id='proglist')
    lis=ids.find_all('li')
    for li in lis :
        
        a=li.find('a')
        href=a['href']
        re1=re.search(r'sc-ad.{0,40}.mp3',href,re.M|re.I)
        if re1:
            add=quote(re1.group())
            web_mp3=url+add
            # print(web_mp3)
            save_url='D:\\mp3\\'
            download(web_mp3,save_url,add)

def download(url,save_url,file_name) :
    try :
        if url is None or file_name is None or save_url is None:
            print("错误")
            return None
        folder=os.path.exists(save_url)
        if not folder :
            os.makedirs(save_url)
        res=requests.get(url,stream=True,timeout=50)
        file_path=os.path.join(save_url,file_name)
        print('开始写入',file_path)
        with open(file_path,'wb') as fd :
            for chunk in res.iter_content() :
                fd.write(chunk)
        print(file_name+'成功下载')
    except :
        print('程序错误')
    
def main() :
    url='http://www.listeningexpress.com/studioclassroom/ad/'
    mp3(url)
if __name__=='__main__' :
    main()