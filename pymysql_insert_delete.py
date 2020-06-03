# -*- encoding: utf-8 -*-
'''
@File : 1.py
@Time : 2020/06/03 00:15:57
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import pymysql
import datetime

# 创建
def create() :
    db = pymysql.connect("localhost","root","root","TESTDB")
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS Messageboard")
    
    sql = """CREATE TABLE Messageboard (
        ID CHAR(20) NOT NULL,
        THEME CHAR(20),
        PERSON CHAR(20),
        TIME Datetime)"""
    cursor.execute(sql)
    db.close()

# 插入
def insert() :
    db = pymysql.connect("localhost","root","root","TESTDB")
    cursor = db.cursor()
    id = input("输入id：")
    theme = input("输入主题:")
    person = input("输入留言人:")
    time = datetime.datetime.now()
    sql = "INSERT INTO Messageboard (ID,THEME,PERSON,TIME) VALUES ('%s','%s','%s','%s')"%(id,theme,person,time)

    try :
        cursor.execute(sql)
        db.commit()
    except :
        db.rollback()
    db.close()

# 删除
def delete() :
    db = pymysql.connect("localhost","root","root","TESTDB")
    cursor = db.cursor()
    id = input("输入要删除的数据ID:")
    sql = "DELETE FROM Messageboard WHERE ID = %s"%(id)
    try :
        cursor.execute(sql)
        db.commit()
    except :
        db.rollback()
    db.close()

# 修改
def update() :
    db = pymysql.connect("localhost","root","root","TESTDB")
    cursor = db.cursor()
    # s1 = input("输入要修改的项:")
    # s3 = input("输入选择修改的项：")
    s4 = input("输入要修改ID的值:")
    s2 = input("输入THEME修改后的值：")
    time1 = datetime.datetime.now()
    sql = "UPDATE Messageboard SET THEME = '%s',TIME = '%s' WHERE ID = %s"%(s2,time1,s4)
    try :
        cursor.execute(sql)
        db.commit()
    except :
        db.rollback()
    db.close()

# 查找
def search() :
    db = pymysql.connect("localhost","root","root","TESTDB")
    cursor = db.cursor()
    id = input("输入查询的ID:")
    sql = "SELECT * FROM Messageboard WHERE ID = %s"%(id)
    try :
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        db.commit()
    except :
        db.rollback()
    db.close()

def menu() :
    print('-----------------------')
    print(' 1.创建表    2.插入')
    print(' 3.删除      4.修改')
    print(' 5.查询      0.退出')
    print('-----------------------')

if  __name__=='__main__' :
    menu()
    a=1
    while(a) :
        a=int(input("输入要选择的序号:"))
        if a==1 :
            create()
        elif a==2 :
            insert()
        elif a==3 :
            delete()
        elif a==4 :
            update()
        elif a==5 :
            search()
        else :
            exit(0)

    
