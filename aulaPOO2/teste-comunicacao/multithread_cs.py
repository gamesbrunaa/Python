import socket
from ssl import SOL_SOCKET
import threading

class clientThread(threading.Thread):

    def __init__(self, addres, socket):
        threading.Thread.__init__(self)
        self.csocket = socket
        self.addres = addres
        print("Nova conexão: ", addres)

    def run(self):
        print("Conectado de: ", addres)
        msg = ''
        while True:
            data = self.csocket.recv(1024)
            msg = data.decode()
            print("from client: ", msg)
            if msg == 'bye':
                break
        print("Client at ", addres, " disconnected...")

if __name__ == '__main__':
    host = ''
    port = 8000
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    print("Servidor iniciado!")
    print("Aguardando nova conexao...")
    while True:
        server.listen(1)
        clientsock, addres = server.accept()
        newthread = clientThread(addres, clientsock)
        newthread.start()