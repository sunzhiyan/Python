# -*- encoding: utf-8 -*-
'''
@File : 2.py
@Time : 2020/03/24 22:27:56
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
lines=[]
num=1
try :
    with open('input.txt','r',encoding='utf8') as f :
        for line in f.readlines() :
            print("第"+str(num)+"行:"+line.strip())
            num=num+1
            lines.append(line.strip())
    print(lines)
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])