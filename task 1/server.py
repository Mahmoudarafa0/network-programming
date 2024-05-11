from socket import *

try:
    server_socket = socket(AF_INET, SOCK_STREAM)
    host = "127.0.0.1"
    port = 1234
    server_socket.bind((host, port))
    server_socket.listen(5)
    client, addr = server_socket.accept()
    print("connection from ", addr[0])
    
    while True:
        x = client.recv(2048)
        if not x:
            break
        received_message = ""
        while True:
            received_message += x.decode("utf-8")
            if len(x) < 2048:
                break
            x = client.recv(2048)
        if received_message == "q":
            break
        print("client: ", received_message)
        y = input("server: ")
        client.send(y.encode("utf-8"))
        
    server_socket.close()
    print("connection closed")

except error as e:
    print(e)
