# -*- encoding: utf-8 -*-
'''
@File : 4.py
@Time : 2020/05/14 20:36:05
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib

# 线程改为进程

from multiprocessing import Process
import socket

def send_msg(udp_socket) :
    while True :
        msg=input('\n请输入要发送的数据:')
        dest_ip=input('\n请输入对方的ip地址:')
        dest_port=int(input('\n请输入对方的port:'))
        udp_socket.sendto(msg.encode('utf_8'),(dest_ip,dest_port))

# 接收数据
def recv_msg(udp_socket) :
    while True :
        recv_msg=udp_socket.recvfrom(1024)
        recv_ip=recv_msg[1]
        recv_msg=recv_msg[0].decode('utf_8')
        print('>>>%s:%s'%(str(recv_ip),recv_msg))

def main() :
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.bind(("",7890))

# 创建进程接收数据
    p=Process(target=recv_msg,args=(udp_socket,))
    p.start()
    send_msg(udp_socket)

if __name__=='__main__' :
    main()
