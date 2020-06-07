# -*- encoding: utf-8 -*-
import traceback

import pymysql
import datetime


# 创建
def create():
    db = pymysql.connect("localhost", "root", "root", "testdb")
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS Messageboard")

    sql = """CREATE TABLE Messageboard (
        ID CHAR(20) NOT NULL,
        THEME CHAR(20),
        PERSON CHAR(20),
        TIME Datetime,
        is_delete int)"""
    try:
        cursor.execute(sql)
    except Exception as e:
        # 异常信息的处理：1直接抛出；2 打印提示输出
        # raise e
        print("发生异常", e)
        # 输出异常信息
        traceback.print_exc()
        # 3 将错误日志输入到目录文件中  
        f = open("log.txt", "a")
        traceback.print_exc(file=f)
        f.flush()
        f.close()
        # # 如果发生错误则回滚
        db.rollback()

    finally:
        # 关闭数据库连接
        db.close()


# 插入
def insert():
    db = pymysql.connect("localhost", "root", "root", "TESTDB")
    cursor = db.cursor()
    id1 = input("输入id：")
    theme = input("输入主题:")
    person = input("输入留言人:")
    is_delete = input("输入是否删除0/1")
    time = datetime.datetime.now()
    sql = "INSERT INTO Messageboard (ID,THEME,PERSON,TIME,is_delete) VALUES ('%s','%s','%s','%s','%s')" % (id1, theme, person, time, is_delete)

    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        # 异常信息的处理：1直接抛出；2 打印提示输出
        # raise e
        print("发生异常",e)
        # 输出异常信息
        traceback.print_exc()
        # 3 将错误日志输入到目录文件中  
        f = open("log.txt", "a")
        traceback.print_exc(file=f)
        f.flush()
        f.close()
        # # 如果发生错误则回滚
        db.rollback()

    finally:
        # 关闭数据库连接
        db.close()


# 删除
def delete():
    db = pymysql.connect("localhost", "root", "root", "TESTDB")
    cursor = db.cursor()
    id1 = input("输入要删除的数据ID:")
    sql = "DELETE FROM Messageboard WHERE ID = %s" % id1
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        # 异常信息的处理：1直接抛出；2 打印提示输出
        # raise e
        print("发生异常", e)
        # 输出异常信息
        traceback.print_exc()
        # 3 将错误日志输入到目录文件中  
        f = open("log.txt", "a")
        traceback.print_exc(file=f)
        f.flush()
        f.close()
        # # 如果发生错误则回滚
        db.rollback()

    finally:
        # 关闭数据库连接
        db.close()


# 修改
def update():
    db = pymysql.connect("localhost", "root", "root", "TESTDB")
    cursor = db.cursor()
    # s1 = input("输入要修改的项:")
    # s3 = input("输入选择修改的项：")
    s4 = input("输入要修改ID的值:")
    s2 = input("输入THEME修改后的值：")
    time1 = datetime.datetime.now()
    sql = "UPDATE Messageboard SET THEME = '%s',TIME = '%s' WHERE ID = %s" % (s2, time1, s4)
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        # 异常信息的处理：1直接抛出；2 打印提示输出
        # raise e
        print("发生异常", e)
        # 输出异常信息
        traceback.print_exc()
        # 3 将错误日志输入到目录文件中  
        f = open("log.txt", "a")
        traceback.print_exc(file=f)
        f.flush()
        f.close()
        # # 如果发生错误则回滚
        db.rollback()

    finally:
        # 关闭数据库连接
        db.close()


# 查找
def search():
    db = pymysql.connect("localhost", "root", "root", "TESTDB")
    cursor = db.cursor()
    id1 = input("输入查询的ID:")
    sql = "SELECT * FROM Messageboard WHERE ID = %s" % id1
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        db.commit()
    except Exception as e:
        # 异常信息的处理：1直接抛出；2 打印提示输出
        # raise e
        print("发生异常", e)
        # 输出异常信息
        traceback.print_exc()
        # 3 将错误日志输入到目录文件中  
        f = open("log.txt", "a")
        traceback.print_exc(file=f)
        f.flush()
        f.close()
        # # 如果发生错误则回滚
        db.rollback()

    finally:
        # 关闭数据库连接
        db.close()


def menu():
    print('-----------------------')
    print(' 1.创建表    2.插入')
    print(' 3.删除      4.修改')
    print(' 5.查询      0.退出')
    print('-----------------------')


if __name__ == '__main__':
    menu()
    a = 1
    while a:
        a = int(input("输入要选择的序号:"))
        if a == 1:
            create()
        elif a == 2:
            insert()
        elif a == 3:
            delete()
        elif a == 4:
            update()
        elif a == 5:
            search()
        else:
            exit(0)

