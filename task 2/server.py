import socket
import threading

def handle_client(client_socket, address, clients):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                clients.remove(client_socket)
                print(f"Client {address} disconnected")
                break
            print(f"Received message from {address}: {message}")
            for client in clients:
                if client != client_socket:
                    client.send(message.encode())
        except:
            clients.remove(client_socket)
            print(f"Client {address} disconnected due to an error")
            break

def main():
    host = '127.0.0.1'
    port = 1234

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    clients = []

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address}")
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address, clients))
        client_thread.start()

if __name__ == "__main__":
    main()
