import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
ADDR = (SERVER, PORT)


def handle_client(conn: socket.socket, addr):
    print(f'[NEW CONNNECTION] {addr} connected')
    while True:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length == '':
            continue
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        if msg == DISCONNECT_MESSAGE:
            break
        print(f'[{addr}] {msg}')
    conn.close()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"server is listening on {SERVER}:{PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS]: {threading.activeCount() - 1}')


if __name__ == "__main__":
    main()
