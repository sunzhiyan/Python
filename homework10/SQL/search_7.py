# -*- encoding: utf-8 -*-
import pymysql

db = pymysql.connect("localhost", "root", "root", "test")
cursor = db.cursor()
student_sql1 = "SELECT * FROM students WHERE gender = '女'"
classes_sql1 = "SELECT * FROM classes WHERE gender = '女'"

try:
    cursor.execute(student_sql1)
    results_student1 = cursor.fetchall()

    cursor.execute(classes_sql1)
    results_classes1 = cursor.fetchall()

    print("students表中女生的总数：")
    print(len(results_student1))

    print("classes表中女生的总数：")
    print(len(results_classes1))

    db.commit()
except:
    db.rollback()
db.close()
