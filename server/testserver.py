import socket

host = ''
port = 2308

replay = 'yes'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

s.listen(3)

conn, attr = s.accept()

request = conn.recv(1024)

print('request is:', request)
print('connected by', attr)

conn.sendall(replay.encode())

s.close()
