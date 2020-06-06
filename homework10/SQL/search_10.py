# -*- encoding: utf-8 -*-
import pymysql

db = pymysql.connect("localhost", "root", "root", "test")
cursor = db.cursor()
student_sql1 = "SELECT gender,group_concat(name) FROM students GROUP BY gender"
classes_sql1 = "SELECT gender,group_concat(name) FROM classes GROUP BY gender"

try:
    cursor.execute(student_sql1)
    results_student1 = cursor.fetchall()

    cursor.execute(classes_sql1)
    results_classes1 = cursor.fetchall()

    sum_student = 0
    sum_classes = 0
    print("students表按性别分组：")
    for result in results_student1:
        print(result)

    print("classes表按性别分组：")
    for result in results_classes1:
        print(result)

    db.commit()
except:
    db.rollback()
db.close()
