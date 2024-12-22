import socket

ip = '0.0.0.0'  # Listen on all interfaces
port = 4401
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSocket.bind((ip, port))
tcpSocket.listen(5)

print("Server is listening on port", port)

while True:
    client, addr = tcpSocket.accept()
    print("Got connection from", addr)
    client.send(b"Hello Tehran")  # Send greeting message
    client.close()
