# -*- encoding: utf-8 -*-
'''
@File : 3.py
@Time : 2020/04/20 23:38:53
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
class dictclass :
    list1=[]
    def __init__(self,n) :
        self.list1=n
    def del_dict(self,key) :
        find_flag=False
        for line in self.list1 :
            if line['key']==key :
                find_flag=True
                self.list1.remove(line)
        if find_flag :
            print("删除成功")
            print(self.list1)
        else :
            print("not found")
    def get_dict(self,key) :
        find_flag=False
        for line in self.list1 :
            if line['key']==key :
                find_flag=True
                print(line['value'])
        if find_flag :
            print("查找成功")
        else :
            print("not found")
    def get_key(self) :
        list2=[]
        for line in self.list1 :
            list2.append(line['key'])
        return list2
    def update_dict(self,list) :
        for line in list :
            self.list1.append(line)
        print("合并后的字典为:",self.list1)
list1=[{'key' :'a','value' : '1'},{'key' :'b','value' : '2'},{'key' :'c','value' : '3'}]
list2=[{'key' :'d','value' : '4'},{'key' :'e','value' : '5'}]
dict=dictclass(list1)
dict.del_dict('a')
dict.get_dict('b')
print("返回列表的键",dict.get_key())
dict.update_dict(list2)
