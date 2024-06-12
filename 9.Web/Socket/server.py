import socket

host = "127.0.0.1"  # адресс локального хоста
port = 2000  # порт

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

server.listen()

while True:
    user, adres = server.accept()
    user.send("connect".encode("utf-8"))

    data = user.recv(1024)
    print(data.decode("utf-8"))
