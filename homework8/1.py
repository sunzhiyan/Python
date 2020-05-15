# -*- encoding: utf-8 -*-
'''
@File : 1.py
@Time : 2020/05/05 19:08:59
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
from multiprocessing import Pool
import sys
import random 
import threading
number=[]
for i in range(100) :
    num=random.randint(0,100)
    number.append(num)
# print(number)
mutex=threading.Lock()
li_it=iter(number)

class MyThread(threading.Thread) :
    def run(self) :
        for i in range(int(len(number)/5)) :
            mutex.acquire()
            msg=self.name
            print(msg,end=' ')
            # it()
            print(next(li_it))
            mutex.release()
def test() :
    for i in range(5) :
        t=MyThread()
        t.start()

def worker(msg,num) :
    print(msg,"执行完毕",number[num])
    num=num+1

def test_pool() :
    po=Pool(5)
    for i in range(len(number)) :
        Pool().apply_async(worker,(i,0,))
    
    po.close()
    po.join()
    

    
if __name__=='__main__' :
    print('线程')
    test()
    print('进程')
    test_pool()



