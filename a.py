# -*- encoding: utf-8 -*-
'''
@File : 实例.py
@Time : 2020/03/04 08:40:44
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
name = input("name:")
age = input("age:")
skill = input("skill:") 
salary = input("salary:") 
info = ''' --- info of ''' + name + ''' name: ''' + name + ''' age: ''' + age + ''' skill: ''' + skill + ''' salary: ''' + salary + ''' ''' 
print(info)


name = input("name:")
age = input("age:")
skill = input("skill:")
salary = input("salary:")
info1 = ''' --- info of %s --- Name:%s Age:%s Skill:%s Salary:%s ''' % (name,name,age,skill,salary)
print(info1)


name = input("username：")
age = input("age：")
skill = input("skill：")
salary = input("salary：")
info = ''' --- info of {_name} Name：{_name} Age：{_age} Skill：{_skill} Salary：{_salary} '''.format(_name=name, _age=age, _skill=skill, _salary=salary) 
print(info)

name = input("name：")
age = input("age：")
skill = input("skill：")
salary = input("salary：")
info = ''' --- info of {0}--- Name：{0} Age：{1} Skill：{2} Salary：{3} '''.format(name, name, age, skill, salary)
print(info)