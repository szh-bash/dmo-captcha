# -*- coding: UTF-8 -*-
# 文件名：server.py
import time
import socket
# import multiprocessing
from service.recognize_vgg16 import predict


def link_handler(link, client):
    """
    该函数为进程需要执行的函数，负责具体的服务器和客户端之间的通信工作
    :param link: 当前线程处理的连接
    :param client: 客户端ip和端口信息，一个二元元组
    :return: None
    """
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +
          ("超级护盾已接收来自驯兽师[%s:%s]庇护请求...." % (client[0], client[1])))
    while True:
        filepath = link.recv(1024).decode()
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), end='')
        if filepath == 'exit':
            print("超级护盾已成功帮助驯兽师[%s:%s]击退邪恶数码兽...." % (client[0], client[1]))
            break
        print("超级护盾正在帮助驯兽师[%s:%s]抵御邪恶数码兽...." % (client[0], client[1]))
        captcha = predict(filepath)
        link.sendall(captcha.encode())
    link.close()


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 4444))
    s.listen(5)
    print('超级护盾已部署，等待驯兽师们的庇护请求...')
    while True:
        # try:
        cnn, addr = s.accept()
        # m = multiprocessing.Process(target=link_handler, args=(cnn, addr, ))
        # m.daemon = True
        # m.start()
        link_handler(cnn, addr)
