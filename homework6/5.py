# -*- encoding: utf-8 -*-
'''
@File : 5.py
@Time : 2020/04/22 23:16:24
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import random
class dog :
    name=''
    hp=0
    ad=0
    def __init__(self,n,h,a) :
        self.name=n
        self.hp=h
        self.ad=a
    def stack_dog(self,people) :
        people.hp-=self.ad
        people.ad=people.ad-2
        print(self.name,"攻击了",people.name)
class people :
    name=''
    hp=0
    ad=0
    def __init__(self,n,h,a) :
        self.name=n
        self.hp=h
        self.ad=a
    def stack_people(self,dog) :
        dog.hp-=self.ad
        dog.ad=dog.ad-3
        print(self.name,"攻击了",dog.name)

dog1=dog('狗1',80,15)
dog2=dog('狗2',80,15)
dog3=dog('狗3',80,15)
people1=people('人1',100,10)
people2=people('人2',100,10)
list1=['dog','people']
list_dog=[dog1,dog2,dog3]
list_people=[people1,people2]
choice=random.choice(list1)
if choice=='dog' :
    while len(list_dog) or len(list_people) :
        Dog=random.choice(list_dog)
        Peo=random.choice(list_people)
        Dog.stack_dog(Peo)
        if Peo.hp==0 or Peo.ad==0:
            list_people.remove(Peo)
            if len(list_people)==0 :
                print("人输了")
                break
        Dog=random.choice(list_dog)
        Peo=random.choice(list_people)
        Peo.stack_people(Dog)
        if Dog.hp==0 or Dog.ad==0:
            list_dog.remove(Dog)
            if len(list_dog)==0 :
                print("狗输了")
                break
else :
    while len(list_dog) or len(list_people) :
        Dog=random.choice(list_dog)
        Peo=random.choice(list_people)
        Dog.stack_dog(Peo)
        if Peo.hp==0 or Peo.ad==0:
            list_people.remove(Peo)
            if len(list_people)==0 :
                print("人输了")
                break
        Dog=random.choice(list_dog)
        Peo=random.choice(list_people)
        Peo.stack_people(Dog)
        if Dog.hp==0 or Dog.ad==0:
            list_dog.remove(Dog)
            if len(list_dog)==0 :
                print("狗输了")
                break