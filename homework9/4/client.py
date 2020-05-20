# -*- encoding: utf-8 -*-
'''
@File : client.py
@Time : 2020/05/20 17:13:55
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import socket
import threading
import os
import get

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
addr = (get.get_ip(),10000)
s.connect(addr)

def recv_msg() :
    print('连接成功！现在可以接受消息！\n')
    while True :
        try :
            response = s.recv(1024)
            print(response.decode('gbk'))
        except ConnectionResetError :
            print("服务器关闭，聊天以结束!")
            s.close()
            break
    os._exit(0)

def send_msg() :
    print('连接成功！现在可以发送消息！\n')
    print("输入消息按回车发送")
    print('输入esc来退出聊天')
    while True :
        msg = input()
        if msg == 'esc' :
            print("你退出聊天")
            s.close()
            break
        s.send(msg.encode('gbk'))
    os._exit(0)

threads = [threading.Thread(target=recv_msg),threading.Thread(target=send_msg)]
for t in threads :
    t.start()