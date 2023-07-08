import socket

host = '127.0.0.1'  # mesmo local do servidor
porta = 8800        # mesma porta do servidor

# Criação do socket
soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Estabelecimento da conexão com o servidor
envio = (host, porta)
soquete.connect(envio)

print('Digite: S e pressione ENTER para encerrar...')
print('DIGITE A MENSAGEM:')
mensagem = input()

while mensagem not in ('s', 'S'):
    # Envio da mensagem para o servidor
    soquete.send(str(mensagem).encode())
    mensagem = input()
    if mensagem in ('s', 'S'):
        break

# Encerramento da conexão
soquete.close()