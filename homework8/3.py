# -*- encoding: utf-8 -*-
'''
@File : 3.py
@Time : 2020/05/13 18:35:14
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
from multiprocessing import Pool
import time

def prime_num() :
    num=0
    time_start=time.time()
    for i in range(2,100000) :
        for j in range(2,i) :
            if i%j==0 :
                break
        else :
            num=num+1
    time_end=time.time()
    print(num,time_end-time_start)


def worker(msg,i,num) :
    for j in range(2,i) :
        if i % j == 0 :
            return num
            break
    else :
        num=num+1
        return num

def test_pool_1() :
    po=Pool(4)
    j=0
    for i in range(100000-2) :
        Pool().apply_async(worker,(i,i+2,j))
        j=worker(i,i+2,j)
    print(j,' ',end='')
    po.close()
    po.join()

def test_pool_2() :
    po=Pool(10)
    j=0
    for i in range(100000-2) :
        Pool().apply_async(worker,(i,i+2,j))
        j=worker(i,i+2,j)
    print(j,' ',end='')
    po.close()
    po.join()
    

if __name__=='__main__' :
    print('不使用多进程')
    prime_num()

    print('4个进程时间：')
    time_start=time.time()
    test_pool_1()
    time_end=time.time()
    print(time_end-time_start)

    print('10个进程时间')
    time_start1=time.time()
    test_pool_2()
    time_end1=time.time()
    print(time_end1-time_start1)
    

