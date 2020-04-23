# -*- encoding: utf-8 -*-
'''
@File : 1.py
@Time : 2020/04/19 00:17:56
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
class dog() :
    
    color=''
    num=0
    path=''
    def __init__(self,n,a,w) :
        self.color=n
        self.num=a
        self.path=w
        self.list1=[{'color' : 'yello','num' : 10,'price' : 20},{'color' : 'red','num' : 15,'price' : 15},{'color' : 'green','num' : 20,'price' : 10}]
    def pri(self) :
        global list1
        for i in range(len(self.list1)) :
            if self.list1[i]['color']==self.color :
                if self.path=='买' :
                    self.list1[i]['num']=self.list1[i]['num']+self.num
                else :
                    self.list1[i]['num']=self.list1[i]['num']-self.num
        print(self.color,"的狗",self.path,self.num,"只")
        print(self.list1)
dog1=dog('yello',3,'买')    
dog1.pri()  
dog2=dog('red',5,'卖')   
dog2.pri()  