# -*- encoding: utf-8 -*-
'''
@File : 6.py
@Time : 2020/04/28 12:56:16
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
try :
    with open('《老人与海》[英文版].txt','r',encoding='utf_8') as f :
        str1=f.read()
        print('sdscf')
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
for i in range(20) :
    print(list1[i])