import socket


def createServer():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind('localhost', 9000)
        server_socket.listen(5)
        while True:
            client_socket, address = server_socket.accept()
            rd = client_socket.recv(1024).decode()
    except:
        pass
