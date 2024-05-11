from socket import *

try:
    client_socket = socket(AF_INET, SOCK_STREAM)
    host = "127.0.0.1"
    port = 1234
    client_socket.connect((host, port))

    while True:
        y = input("client: ")
        client_socket.send(y.encode("utf-8"))
        if y == "q":
            break
        received_message = ""
        while True:
            x = client_socket.recv(2048)
            if not x:
                break
            received_message += x.decode("utf-8")
            if len(x) < 2048:
                break
        print("server: ", received_message)

    client_socket.close()
    print("connection closed")

except error as e:
    print(e)
