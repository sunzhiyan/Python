# -*- encoding: utf-8 -*-
'''
@File : 7.py
@Time : 2020/04/28 12:54:08
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import jieba
try :
    with open('三国演义_第一卷(第1章-20章).txt','r') as f :
        str1=f.read()
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
words=jieba.lcut(str1)
counts={}
for word in words :
    if len(word) ==1 :
        continue
    else :
        counts[word]=counts.get(word,0)+1

list1=list(counts.items())
list1.sort(key=lambda x:x[1],reverse=True)

for i in range(10) :
    word,count=list1[i]
    print("{0:<5}{1:>5}".format(word,count))
        
