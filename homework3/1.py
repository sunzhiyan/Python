# -*- encoding: utf-8 -*-
'''
@File : 1.py
@Time : 2020/03/24 21:50:31
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
lines=[]
print("输入多行文本，")
while True :
    s=input()
    if s=='' :
        break
    try :
        lines.append(s)
    except :
        break
try :
    f=open("input.txt",'w')
    for i in range(len(lines)) :
        f.write(lines[i]+'\n')
    f.close()
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
