# -*- encoding: utf-8 -*-
import pymysql

db = pymysql.connect("localhost", "root", "root", "test")
cursor = db.cursor()
student_sql1 = "SELECT * FROM students"
classes_sql1 = "SELECT * FROM classes"

try:
    cursor.execute(student_sql1)
    results_student1 = cursor.fetchall()

    cursor.execute(classes_sql1)
    results_classes1 = cursor.fetchall()

    sum_student = 0
    sum_classes = 0
    print("students表中学生平均年龄：")
    for result in results_student1:
        sum_student = result[2] + sum_student
    print(int(sum_student/len(results_student1)))

    print("classes表中学生平均年龄：")
    for result in results_classes1:
        sum_classes = result[2] + sum_classes
    print(int(sum_classes/len(results_classes1)))

    db.commit()
except:
    db.rollback()
db.close()
