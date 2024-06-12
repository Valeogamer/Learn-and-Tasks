import socket
import threading

def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(f"Server: {data.decode()}")
        except ConnectionResetError:
            break
    sock.close()

def send_messages(sock):
    while True:
        message = input()
        if message.lower() == 'exit':
            break
        sock.sendall(message.encode())
    sock.close()

def start_tcp_client(host='127.0.0.1', port=2000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print(f"Connected to {host}:{port}")

        # Create threads for sending and receiving messages
        receive_thread = threading.Thread(target=receive_messages, args=(s,))
        send_thread = threading.Thread(target=send_messages, args=(s,))

        receive_thread.start()
        send_thread.start()

        receive_thread.join()
        send_thread.join()

if __name__ == "__main__":
    start_tcp_client()
