# -*- encoding: utf-8 -*-
'''
@File : 2.py
@Time : 2020/05/09 20:18:25
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import threading
import requests
import random
import sys
import re

url_list=[]
mutex=threading.Lock()
li_it=iter(url_list)

try :
    with open('url_data.txt','r') as f :
        for lines in f.readlines() :
            li=re.findall(r'http://[0-9a-zA-Z_.-]{0,40}',lines,re.M|re.I)
            for i in range(len(li)) :
                url_list.append(li[i])
            
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])

def getHtmlText(url) :
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
    with open('url_data_1.txt','a') as f1 :
        try :
            r=requests.get(url,headers,timeout=30)
            response=r.status_code
            if response==200 :
                print(url+'可访问')
                f1.write(url+'可访问'+'\n')
            else :
                print(url+response+'不可访问')
                f1.write(url+response+'不可访问'+'\n')
        except Exception as e :
            print(url,e,'不可访问')
            f1.write(url+'不可访问'+'\n')

class MyThread(threading.Thread) :
    def run(self) :
        for i in range(int(len(url_list)/20)) :
            mutex.acquire() 
            msg=self.name
            print(msg)
            getHtmlText(next(li_it))
            mutex.release()

def test() :
    for i in range(20) :
        t=MyThread()
        t.start()

if __name__=='__main__' :
    print('数据保存入url_data_1.txt中')
    test()
