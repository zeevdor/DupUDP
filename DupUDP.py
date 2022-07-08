import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
txsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

localaddr = ("192.168.1.10",5000)
sock.bind(localaddr)

while 1:
 data,addr = sock.recvfrom(1500000)
 txsock.sendto(data,("127.0.0.1",5010))
 txsock.sendto(data,("192.168.1.100",5010))
