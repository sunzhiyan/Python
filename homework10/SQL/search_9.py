# -*- encoding: utf-8 -*-
import pymysql

db = pymysql.connect("localhost", "root", "root", "test")
cursor = db.cursor()
student_sql1 = "SELECT * FROM students WHERE gender = '男'"
student_sql2 = "SELECT * FROM students WHERE gender = '女'"
classes_sql1 = "SELECT * FROM classes WHERE gender = '男'"
classes_sql2 = "SELECT * FROM classes WHERE gender = '女'"

try:
    cursor.execute(student_sql1)
    results_student1 = cursor.fetchall()
    cursor.execute(student_sql2)
    results_student2 = cursor.fetchall()

    cursor.execute(classes_sql1)
    results_classes1 = cursor.fetchall()
    cursor.execute(classes_sql2)
    results_classes2 = cursor.fetchall()

    sum_student1 = 0
    sum_student2 = 0
    sum_classes1 = 0
    sum_classes2 = 0
    print("students表中男学生平均年龄：")
    for result in results_student1:
        sum_student1 = result[2] + sum_student1
    print(int(sum_student1/len(results_student1)))

    print("students表中女学生平均年龄：")
    for result in results_student2:
        sum_student2 = result[2] + sum_student2
    print(int(sum_student2 / len(results_student2)))

    print("classes表中男学生平均年龄：")
    for result in results_classes1:
        sum_classes1 = result[2] + sum_classes1
    print(int(sum_classes1/len(results_classes1)))

    print("classes表中女学生平均年龄：")
    for result in results_classes2:
        sum_classes2 = result[2] + sum_classes2
    print(int(sum_classes2 / len(results_classes2)))

    db.commit()
except:
    db.rollback()
db.close()
