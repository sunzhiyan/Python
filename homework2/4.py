# -*- encoding: utf-8 -*-
'''
@File : 4.py
@Time : 2020/03/10 22:54:04
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
def str(s,count1,count2,count3,count4) :
    for i in range(len(s)):
        if s[i]>'a' and s[i]<'z' or s[i]>'A' and s[i]<'Z' :
            count1=count1+1
        else : 
            if s[i]>'0' and s[i]<'9' :
                count2=count2+1
            else :
                if s[i]==' ' :
                    count3=count3+1
                else :
                    count4=count4+1
    print("字母:",count1,"个\n数字:",count2,"个\n空格：",count3,"个\n其他字符:",count4)
count1=0
count2=0
count3=0
count4=0
print("输入一段字符串:")
str1=input()
str(str1,count1,count2,count3,count4)

        
