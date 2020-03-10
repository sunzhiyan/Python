# -*- encoding: utf-8 -*-
'''
@File : 9.py
@Time : 2020/03/10 21:18:45
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
a=int(input("输入被猜数字:"))
N=int(input("输入最多猜错次数:"))
for i in range(0,N) :
    b=int(input("输入猜的数"))
    if a==b :
        print("猜测正确，游戏成功")
        break
    else :
        print("猜测失败，请继续输入:")
else :
    print("游戏结束，你失败了")