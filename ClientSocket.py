from socket import *


while True:
    serverName = "127.0.0.1"
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    sentence = input('Input Random;tal1;tal2, Add;tal1;tal2, or Subtract;tal1;tal2: or quit \n INPUT HERE: ')
    if (sentence == "quit"):
        print("stopping")
        break
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print('From server: ', modifiedSentence.decode())