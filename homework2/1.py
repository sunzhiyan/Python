# -*- encoding: utf-8 -*-
'''
@File : 1.py
@Time : 2020/03/10 21:59:55
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
def test(num):
    print("相应的长度为:")
    print(len(num))
test_num = eval(input("请输入字符串，列表或元组,字符串请加上引号："))
test(test_num)