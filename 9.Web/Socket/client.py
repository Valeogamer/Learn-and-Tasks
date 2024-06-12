import socket

host = "127.0.0.1"
port = 2000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((host, port))

while True:
    data = client.recv(1024)
    print(data.decode("utf-8"))

    client.send(input().encode("utf-8"))
