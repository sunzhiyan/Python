# -*- encoding: utf-8 -*-
'''
@File : 3_client.py
@Time : 2020/05/20 00:13:00
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
from socket import *

udp_socket = socket(AF_INET,SOCK_DGRAM)

local_addr = ('192.168.1.104',8080)
udp_socket.bind(local_addr)

while True :
    recv_data = udp_socket.recvfrom(1024)

    recv_result = recv_data[0].decode('gbk')
    print(recv_result)

    print(recv_data[1])

    if recv_result == 'stop' :
        break

udp_socket.close()

