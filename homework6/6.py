# -*- encoding: utf-8 -*-
'''
@File : 6.py
@Time : 2020/04/23 16:49:13
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
class student :
    classroom=''
    num=''
    name=''
    python=0
    def __init__(self,c,n,na,p) :
        self.classroom=c
        self.num=n
        self.name=na
        self.python=p
class Menu :
    def __init__(self) :
        pass
    def menu() :
        print('--------学生管理系统--------')
        print('   1、增加学生信息')
        print('   2、删除学生信息')
        print('   3、修改学生信息')
        print('   4、查询学生信息')
        print('   0、退出')
        print('---------------------------')
    def add() :
        classroom=input('输入学生班级：')
        num=input('输入学生学号：')
        name=input('输入学生姓名：')
        python=int(input('输入学生python成绩：'))
        stu=student(classroom,num,name,python)
        with open('student.txt','a',encoding='utf_8') as f:
            f.write(stu.classroom+' '+stu.num+' '+stu.name+' '+str(stu.python)+'\n')
    def dele() :
        lines=[]
        num=input("输入要删除学生的学号:")
        with open('student.txt','r',encoding='utf_8') as f :
            for line in f.readlines() :
                lines.append(line.split())
        for i in range(len(lines)) :
            if num==lines[i][1] :
                lines.remove(lines[i])
        with open('student.txt','w',encoding='utf_8') as f :
            for i in range(len(lines)) :
                f.write(lines[i][0]+' '+lines[i][1]+' '+lines[i][2]+' '+lines[i][3]+'\n')
        print('删除成功')
    def change() :
        lines=[]
        num=input('输入要修改的学生学号:')
        classroom=input('输入修改后学生班级：')
        num=input('输入修改后学生学号：')
        name=input('输入修改后学生姓名：')
        python=input('输入修改后学生python成绩：')
        stu=student(classroom,num,name,python)
        with open('student.txt','r',encoding='utf_8') as f :
            for line in f.readlines() :
                lines.append(line.split())
        print(lines)
        for i in range(len(lines)) :
            if num==lines[i][1] :
                lines[i][0]=student.classroom
                lines[i][1]=student.num
                lines[i][2]=student.name
                lines[i][3]=student.python
        with open('student.txt','w',encoding='utf_8') as f :
            for i in range(len(lines)) :
                f.write(lines[i][0]+' '+lines[i][1]+' '+lines[i][2]+' '+lines[i][3]+'\n')
    def search() :
        lines=[]
        num=input("输入要查询的学生学号:")
        with open('student.txt','r',encoding='utf_8') as f :
            for line in f.readlines() :
                lines.append(line.split())
        for i in range(len(lines)) :
            if num==lines[i][1] :
                print("班级：",lines[i][0],"学号:",lines[i][1],"姓名:",lines[i][2],"python成绩:",lines[i][3])
    def exit() :
        print('退出')
        exit()
Menu.menu()
while True :
    choice=int(input('选择功能:'))
    if choice==1 :
        Menu.add()
    elif choice==2 :
        Menu.dele()
    elif choice==3 :
        Menu.change()
    elif choice==4 :
        Menu.search()
    elif choice==0 :
        Menu.exit()
    else :
        print("输入有误") 

        

