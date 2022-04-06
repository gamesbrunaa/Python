from http import client
import socket

ip = 'localhost'
port = 8000
addr = ((ip, port))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)

receber = ''
while(receber != 'sair'):
    msg = input('digite uma mensagem para o servidor: ')
    client_socket.send(msg.encode())
    #print('mensagem enviada')
    receber = client_socket.recv(1024).decode()
    print('mensagem recebida: ' + receber)

client_socket.close()