# -*- encoding: utf-8 -*-
import pymysql

db = pymysql.connect("localhost", "root", "root", "test")
cursor = db.cursor()
student_sql1 = "SELECT * FROM students WHERE name like '黄_'"
classes_sql1 = "SELECT * FROM classes WHERE name like '黄_'"

try:
    cursor.execute(student_sql1)
    results_student1 = cursor.fetchall()

    cursor.execute(classes_sql1)
    results_classes1 = cursor.fetchall()

    print("students表中姓为黄名只有一个字的学生：")
    for result in results_student1:
        print('name:', result[1], 'age:', result[2], 'class:', result[5])

    print("classes表中姓为黄名只有一个字的学生：")
    for result in results_classes1:
        print(result)

    db.commit()
except:
    db.rollback()
db.close()
