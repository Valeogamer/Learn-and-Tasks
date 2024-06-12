import socket
import threading

def handle_client(conn, addr):
    print(f"Подключен {addr}")
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Получен от {addr}: {data.decode()}")
            conn.sendall(data)
        except ConnectionResetError:
            break
    print(f"Соединение с {addr} отключено.")
    conn.close()

def start_tcp_server(host='127.0.0.1', port=2000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Сервер слушает {host}:{port}")
        while True:
            conn, addr = s.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()

if __name__ == "__main__":
    start_tcp_server()

