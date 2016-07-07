import socket
import struct

multicast_addr = '224.0.0.1'
bind_addr = '0.0.0.0'
port = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
membership = socket.inet_aton(multicast_addr) + socket.inet_aton(bind_addr)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, membership)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind((bind_addr, port))

while True:
    message, address = sock.recvfrom(255)
    print message, address
