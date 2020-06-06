# -*- encoding: utf-8 -*-
import pymysql

db = pymysql.connect("localhost", "root", "root", "test")
cursor = db.cursor()
sql = "SELECT * FROM students WHERE gender = '男'"
sql1 = "SELECT * FROM classes WHERE gender = '男'"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.execute(sql1)
    results1 = cursor.fetchall()
    print("students表男生：")
    for result in results:
        print('name:', result[1], 'age:', result[2], 'class:', result[5])
    print("classes表男：")
    for result in results:
        print(result)
    db.commit()
except:
    db.rollback()
db.close()
