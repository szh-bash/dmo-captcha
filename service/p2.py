#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：client.py
import socket
import time

ip_port = ('127.0.0.1', 4444)
s = socket.socket()
s.connect(ip_port)
print('connected')
while True:
    inp = input().strip()
    timer = time.time()
    if not inp:
        continue
    s.sendall(inp.encode())
    if inp == 'exit':
        break
    server_reply = s.recv(1024).decode()
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +
          '已收到超级护盾给予的神秘代码，成功抵御邪恶数码兽本次进攻： ', end='')
    print(server_reply)
s.close()
