# -*- encoding: utf-8 -*-
'''
@File : server.py
@Time : 2020/05/20 16:58:39
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
import socket
import get
import threading
import os

class ChatSever :
    def __init__(self) :
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.addr = (get.get_ip(),10000)
        self.users = {}

    def start_sever(self) :
        try :
            self.sock.bind(self.addr)
        except Exception as e :
            print(e)
        self.sock.listen(5)
        print('服务器已开启，等待链接---')
        print('在空白出输入stop关闭服务器')

        self.accept_cont()

    def accept_cont(self) :
        while True :
            s,addr=self.sock.accept()
            self.users[addr] = s
            number = len(self.users)
            print('用户{}连接成功，现在共有{}为用户'.format(addr,number))

            threading.Thread(target=self.recv_send,args=(s,addr)).start()

    def recv_send(self,sock,addr) :
        while True :
            try :
                response = sock.recv(4096).decode('gbk')
                msg = '{}用户{}发来消息'.format(get.get_time(),addr,response)

                for client in self.users.values() :
                    client.send(msg.encode('gbk'))
            except ConnectionResetError :
                print('用户{}已经退出聊天！'.format(addr))
                self.users.pop(addr)
                break

    def close_sever(self) :
        for client in self.users.values() :
            client.close()
        self.sock.close()
        os._exit(0)

if __name__=='__main__' :
    sever = ChatSever()
    sever.start_sever()
    while True :
        cmd = input()
        if cmd == 'stop' :
            sever.close_sever()
        else :
            print('输入命令无效,请重新输入!')