import socket

host = '127.0.0.1'
port = 2308

request = 'can you hear me?'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

s.sendall(request.encode())

replay = s.recv(1024)

print('replay is', replay)
s.close()
