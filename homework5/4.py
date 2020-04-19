# -*- encoding: utf-8 -*-
'''
@File : 4.py
@Time : 2020/04/18 23:33:28
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
def outer_1(func) :
    def inner() :
        print("A")
        func()
    return inner

@outer_1
def func_1() :
    num=[]
    i=2
    for i in range(2,20000) :
        for j in range(2,i) :
            if i%j==0 :
                break
        else :
            num.append(i)
    print(num)


def outer_2(func) :
    def inner() :
        print("B")
        fun=func()
        print("2到10000素数的个数为",fun)
    return inner

@outer_2
def func_2() :
    num=0
    i=2
    for i in range(2,10000) :
        for j in range(2,i) :
            if i%j==0 :
                break
        else :
            num=num+1
    return num


def outer_3(func) :
    def inner() :
        print("C")
        M=int(input("输入M的值:"))
        func(M)
    return inner

@outer_3
def func_3(M) :
    num=0
    i=2
    for i in range(2,M) :
        for j in range(2,i) :
            if i%j==0 :
                break
        else :
            num=num+1
    print("0到",M,"的素数个数为",num)

    
func_1()
func_2()
func_3()