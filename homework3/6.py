# -*- encoding: utf-8 -*-
'''
@File : 6.py
@Time : 2020/03/25 18:53:09
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
try :
    with open('01.txt','r') as f :
        str1=f.read()
    with open('02.txt','r') as f1 :
        str2=f1.read()
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
def wordcount(str) :
    strlist=str.replace('\n',' ').lower().split(' ')
    dict1={}
    for str in strlist :
        if str in dict1.keys() :
            dict1[str]=dict1[str]+1
        else :
            dict1[str]=1
    strlist=sorted(dict1.items(),key=lambda x : x[1],reverse=True)
    return strlist
list1=[]
list1=wordcount(str1)
list2=[]
list2=wordcount(str2)
num=0
for i in range(10) :
    for j in range(10) :
        if list1[i][0]==list2[j][0] :
            num=num+1
num=num*10
print("两文章的相似率为:"+str(num)+'%')