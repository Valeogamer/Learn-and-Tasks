import socket

HOST = "127.0.0.1"
PORT = 2000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # открываем сокет сервера на прием
    s.bind((HOST, PORT))  # адресс и порт сервера, привязываем к сокету
    s.listen(5)  # позволяет принимать входящие соединения
    try:
        while True:
            conn, addr = s.accept()  # блокирует программу до тех пор 
            # пока не соединиться кто нибудь, у которого
            # свой сокет(conn) и свой адресс(addr(host, port))
            with conn:
                print(f"К серверу подключился: {addr}")
                while True:
                    data = conn.recv(1024)  # ожидаем письмо от клиента, буфер 1024байта
                    if not data:
                        break
                    conn.sendall(data)
    except KeyboardInterrupt:
        print("Остановка сервера ...")
    finally:
        s.close()
        print("Сервер отключен.")
