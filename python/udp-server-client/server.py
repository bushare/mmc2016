import random
from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))

while True:
    message, address = serverSocket.recvfrom(1024)
    message = message.upper()
    serverSocket.sendto(message, address)
