from socket import *

serverPort = 3000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))

serverSocket.listen(1)

print('O Servidor ta pronto pra receber as ordens, meu patrão. Digita Ctrl + C que eu dou o vaza.')

def authorizeUser(user):
    user = str(user).replace("b",'').replace("'","")
    userFile = open("users.txt", "r")
    users = userFile.readlines()
    for i in range(len(users)):
        users[i] = users[i].replace('\n','')

    if user in users:
        return True
    else: 
        return False

while True:
    try:
        connectionSocket , addr = serverSocket.accept()
        sentence = connectionSocket.recv(2048)
        sentence = str(sentence).replace("b",'').replace("'","").split(' ')
        if sentence[1] == 'CUMP':
            userAuthorization =  authorizeUser(sentence)
        elif sentence[1] == 'LISTA':
            print('1')
        elif sentence[1] == 'PEGA':
            print('1')
        elif sentence[1] == 'TERM':
            print('1')
        else:
            connectionSocket.send('NOK')
        connectionSocket.close()
    except(KeyboardInterrupt, SystemError):
        break


def teste(req):
    print(req)