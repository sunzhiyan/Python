# -*- encoding: utf-8 -*-
import pymysql

db = pymysql.connect("localhost", "root", "root", "test")
cursor = db.cursor()
student_sql1 = "SELECT * FROM students WHERE gender = '男' and is_delete = 0 ORDER BY age DESC"
classes_sql1 = "SELECT * FROM classes WHERE gender = '男' and is_delete = 0 ORDER BY age DESC"

try:
    cursor.execute(student_sql1)
    results_student1 = cursor.fetchall()

    cursor.execute(classes_sql1)
    results_classes1 = cursor.fetchall()

    print("students表查询未删除男生信息，按年龄降序：")
    for result in results_student1:
        print(result)

    print("classes表中查询未删除男生信息，按年龄降序：")
    for result in results_classes1:
        print(result)

    db.commit()
except:
    db.rollback()
db.close()
