from socket import *


serverName = '127.0.0.1'
serverPort = 3000
clienteSocket = socket(AF_INET, SOCK_STREAM)

clienteSocket.connect((serverName, serverPort))

message = input('Digite uma frase: ')
clienteSocket.send(message.encode('ascii'))

moddmsg, addr = clienteSocket.recvfrom(2048)
print(moddmsg.decode())

clienteSocket.close()