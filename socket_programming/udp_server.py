import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定本地的ip和端口号
# s.bind(('127.0.0.1', '4100'))

# ip地址不用写，会使用当前主机的ip
s.bind(('', 4200))


RECV_MSG_SIZE = 1024
recv_msg = s.recvfrom(1024)
msg = recv_msg[0].decode('utf-8')

response = f'hello, i received your msg: {msg}'.encode('utf-8')
s.sendto(response, ('127.0.0.1', 8080))

print(msg)

s.close()
