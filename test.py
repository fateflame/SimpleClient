import socket

#HOST = '10.26.29.120'    # The remote host
HOST = '127.0.0.1'
PORT = 50017              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
data = s.recv(1024)
print repr(data)
s.sendall('$login abc 123')
data = s.recv(1024)
print (data)
s.close()
