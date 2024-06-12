import socket

def start_tcp_server(host='127.0.0.1', port=65432):
    # Создаем сокет
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # AF_INET используется для адресов IPv4
        # SOCK_STREAM используется для сокетов TCP
        # SOCK_DGRAM используется для сокетов UDP
        # Привязываем сокет к хосту и порту
        s.bind((host, port))
        # Переводим сокет в режим прослушивания
        s.listen()
        print(f"Сервер слушает {host}:{port}")
        # Принимаем соединение
        conn, addr = s.accept()
        with conn:
            print(f"Соединение с {addr}")
            while True:
                # Получаем данные от клиента, размер буфера 1024 байта
                # recv получение данных от клиента
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Получены данные: {data.decode()}")
                # Отправляем данные обратно клиенту (эхо)
                conn.sendall(data)

if __name__ == "__main__":
    start_tcp_server()

