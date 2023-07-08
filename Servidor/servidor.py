import socket
from datetime import datetime

host = '127.0.0.1'  # o mesmo que localhost
porta = 8800         # porta da conexão

# Criação do socket
soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # estou usando TCP/IP

# Vincula o socket ao endereço e porta especificados
recebe = (host, porta)
soquete.bind(recebe)

# Aguarda por conexões
soquete.listen(2)

print('\nSERVIDOR INICIADO...IP:', host, 'PORTA:', porta, 'EM:', datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))

while True:
    # Aceita a conexão do cliente
    conexao, enderecoIP = soquete.accept()
    print('\nSERVIDOR ACESSADO PELO CLIENTE:', enderecoIP, 'EM:', datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))

    while True:
        # Recebe a mensagem do cliente
        mensagem = conexao.recv(2048)
        if not mensagem:
            break
        
        # Decodifica a mensagem recebida
        mensagem_decodificada = mensagem.decode()

        # Exibe informações sobre o cliente e a mensagem recebida
        print('\nIP CLIENTE:', enderecoIP)
        print('MENSAGEM RECEBIDA:', mensagem_decodificada, '-', datetime.now().strftime('%H:%M:%S'))

    print('CONEXÃO COM O CLIENTE FINALIZADA...', enderecoIP, 'EM:', datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))

    # Fecha a conexão com o cliente
    conexao.close()
