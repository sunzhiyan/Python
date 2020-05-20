# -*- encoding: utf-8 -*-
'''
@File : 3_server.py
@Time : 2020/05/20 00:12:52
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import socket

def main() :
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    dest_addr=('192.168.1.104',8080)

    while True :
        send_data=input('请输入要发送的数据:')
        udp_socket.sendto(send_data.encode('utf-8'),dest_addr)

        if send_data=='stop' :
            break

    udp_socket.close()

if __name__=='__main__' :
    main()