import socket

ip = "server"  # Use the service name defined in docker-compose
port = 5230
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
data = s.recv(1024)
print(data.decode('utf-8'))  # Decode the received bytes to string
s.close()