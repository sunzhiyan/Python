# -*- encoding: utf-8 -*-
'''
@File : 1.py
@Time : 2020/05/18 15:34:55
@Author : xdbcb8 
@Version : 1.0
@Contact : xdbcb8@qq.com
@WebSite : www.xdbcb8.com
'''

# here put the import lib
# import socket

# def main() :
#     udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#     dest_addr=('192.168.1.104',8081)
#     send_data=input("请输入要发送的数据:")
#     udp_socket.sendto(send_data.encode('utf_8'),dest_addr)

#     udp_socket.close()

# if __name__=='__main__' :
#     main()

# from socket import *

# def main() :
#     udp_socket=socket(AF_INET,SOCK_DGRAM)

#     local_addr=('',8081)

#     udp_socket.bind(local_addr)
#     recv_data=udp_socket.recvfrom(1024)

#     print(recv_data)

#     udp_socket.close()

# if __name__=='__main__' :
#     main()

# # 服务端
# import socket
# import sys

# serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# host=socket.gethostname()
# port=9999
# serversocket.bind((host,port))
# serversocket.listen(5)

# while True :
#     clientsocket,addr=serversocket.accept()
#     print("连接地址:%s"%str(addr))
#     msg='欢迎访问菜鸟教程!'+"\r\n"
#     clientsocket.send(msg.encode('utf_8'))
#     clientsocket.close()

# # 客户端
# import socket
# import sys

# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# host=socket.gethostname()
# port=9999
# s.connect((host,port))
# msg=s.recv(1024)
# s.close()
# print(msg.decode('utf-8'))

# import socket
# # 创建一个socket:
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# # 建立连接:
# s.connect(('www.sina.com.cn', 80))

# # 发送数据:
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# # 接收数据:
# buffer = []
# while True:
#     # 每次最多接收1k字节:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break

# data = b''.join(buffer)

# # 关闭连接:
# s.close()

# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))

# # 把接收的数据写入文件:
# with open('sina.html', 'wb') as f:
#     f.write(html)


import threading
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(5)
print('waiting for connection----')

while True :
    sock,addr=s.accept()
    t=threading.Thread(target=tcplink,args=(sock,addr))
    t.start()

def tcplink(sock,addr) :
    print('Accept new connection from %s:%s---'%addr)
    sock.send(b'Welcome!')
    while True :
        data=sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf_8')=='exit' :
            break
        sock.send(('hello,%s'%data.decode('utf_8')).encode('utf_8'))
    sock.close()
    print('connection from %s:%s closed'%addr)

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael',b'Tracy',b'Sarah'] :
    s.send(data)
    print(s.recv(1024).decode('utf_8'))

s.send(b'exit')
s.close()