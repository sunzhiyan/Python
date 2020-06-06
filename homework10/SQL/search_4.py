# -*- encoding: utf-8 -*-
import pymysql

db = pymysql.connect("localhost", "root", "root", "test")
cursor = db.cursor()
student_sql1 = "SELECT * FROM students WHERE id in (1,3,8)"
classes_sql1 = "SELECT * FROM classes WHERE id in (1,3,8)"

try:
    cursor.execute(student_sql1)
    results_student1 = cursor.fetchall()

    cursor.execute(classes_sql1)
    results_classes1 = cursor.fetchall()

    print("students表中ID为1,3,8的学生：")
    for result in results_student1:
        print('name:', result[1], 'age:', result[2], 'class:', result[5])

    print("classes表中ID为1,3,8的学生：")
    for result in results_classes1:
        print(result)

    db.commit()
except:
    db.rollback()
db.close()
