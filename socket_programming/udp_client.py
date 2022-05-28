import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定本地的ip和端口号
# s.bind(('127.0.0.1', '4100'))

# ip地址不用写，会使用当前主机的ip
s.bind(('', 4300))

# python3中通过socket发送数据时要求使用bytes类型的数据
s.sendto('hello world!'.encode('utf-8'), ('127.0.0.1', 4200))

recv_msg = s.recvfrom(1024)

print(recv_msg[0].decode('utf-8'))

s.close()
