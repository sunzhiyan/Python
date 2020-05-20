# -*- encoding: utf-8 -*-
'''
@File : 2.py
@Time : 2020/05/19 21:50:30
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
from socket import *

def main() :
    udp_socket=socket(AF_INET,SOCK_DGRAM)
    local_addr=('',9999)
    udp_socket.bind(local_addr)
    recv_data=udp_socket.recvfrom(1024)
    print(recv_data)

    udp_socket.close()

if __name__=='__main__' :
    main()
