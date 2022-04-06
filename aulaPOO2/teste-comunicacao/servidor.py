import socket

host = 'localhost'
port = 8000
addr = (host, port)

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_socket.bind(addr)
serv_socket.listen(10)

print('aguardando conexao...')
conexao, cliente = serv_socket.accept()
print('conectado')
print('aguardando mensagem')

recebe = ''
while(recebe != 'sair'):
    recebe = conexao.recv(1024)
    print('mensagem recebida: '+ recebe.decode())
    enviar = input('digite uma mensagem para enviar ao cliente')
    conexao.send(enviar.encode())

serv_socket.close()