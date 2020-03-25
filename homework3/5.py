# -*- encoding: utf-8 -*-
'''
@File : 5.py
@Time : 2020/03/25 16:54:19
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import os
str='How many roads must a man walk down\n\
Before they call him a man\n\
How many seas must a white dove sail\n\
Before she sleeps in the sand\n\
How many times must the cannon balls fly\n\
Before they re forever banned\n\
The answer my friend is blowing in the wind\n\
The answer is blowing in the wind'
try :
    f=open("Blowing in the wind.txt","w")
    f.write(str)
    f.close()
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])

def read(lines) :
    try :
        with open('Blowing in the wind.txt','r',) as f :
            for line in f.readlines() :
                lines.append(line.strip())
        return lines
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])

def write(lines) :
    try :
        f=open("Blowing in the wind.txt",'w')
        for i in range(len(lines)) :
            f.write(lines[i]+'\n')
        f.close()
        return lines
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])

def insert_singname(lines) :
    str1='Blowin’in the wind'
    read(lines)
    lines.insert(0,str1)
    write(lines)

def insert_people(lines) :
    str2='Bob Dylan'
    read(lines)
    lines.insert(1,str2)
    write(lines)

def insert_end(lines) :
    str3='1962 by Warner Bros. Inc.'
    read(lines)
    lines.append(str3)
    write(lines)

def print1(lines) :
    try :
        with open('Blowing in the wind.txt','r') as f :
            for line in f.readlines() :
                print(line.strip())
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
lines=[]
lines2=[]
lines3=[]
lines4=[]
print("在文件头部插入歌名")
insert_singname(lines)
print("在歌名后插入歌手名")
insert_people(lines2)
print("在文件末尾加入字符串")
insert_end(lines3)
print("打印文件内容")
print1(lines4)