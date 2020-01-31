import socket

ip_address = '10.61.55.63'
port = 5000
buffer = 8
message = ''

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip_address, port))
s.send(message.encode())

s.close()
