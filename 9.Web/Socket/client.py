import socket

def start_tcp_client(host='127.0.0.1', port=65432):
    # Создаем сокет
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Подключаемся к серверу
        s.connect((host, port))
        # Отправляем данные серверу
        s.sendall(b'Hello, world')
        # Получаем ответ от сервера
        data = s.recv(1024)
        print(f"Received {data.decode()}")

if __name__ == "__main__":
    start_tcp_client()
