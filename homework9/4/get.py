# -*- encoding: utf-8 -*-
'''
@File : get.py
@Time : 2020/05/20 16:31:04
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import socket
import datetime

def get_ip() :
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    return ip

def get_time() :
    now = datetime.datetime.now()
    send_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return send_time

    