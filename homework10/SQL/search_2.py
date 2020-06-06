# -*- encoding: utf-8 -*-
import pymysql

db = pymysql.connect("localhost", "root", "root", "test")
cursor = db.cursor()
student_sql1 = "SELECT * FROM students WHERE id < 4"
student_sql2 = "SELECT * FROM students WHERE is_delete = 0"
classes_sql1 = "SELECT * FROM classes WHERE id < 4"
classes_sql2 = "SELECT * FROM students WHERE is_delete = 0"

try:
    cursor.execute(student_sql1)
    results_student1 = cursor.fetchall()
    cursor.execute(student_sql2)
    results_student2 = cursor.fetchall()

    cursor.execute(classes_sql1)
    results_classes1 = cursor.fetchall()
    cursor.execute(classes_sql2)
    results_classes2 = cursor.fetchall()

    print("students表编号小于4：")
    for result in results_student1:
        print('name:', result[1], 'age:', result[2], 'class:', result[5])
    print("students没被删除的学生：")
    for result in results_student2:
        print('name:', result[1], 'age:', result[2], 'class:', result[5])

    print("classes表编号小于4：")
    for result in results_classes1:
        print(result)
    print("classes表没被删除的学生：")
    for result in results_classes2:
        print(result)

    db.commit()
except:
    db.rollback()
db.close()
