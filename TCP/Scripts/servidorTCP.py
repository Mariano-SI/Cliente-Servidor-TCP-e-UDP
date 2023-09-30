'''
Redes de Computadores II - Trabalho 2 

Script Servidor (TCP)

Alunos: Iago Mateus Ávila Fernandes, Lucas Alexsander Barbosa Cruz, Mariano Carlos Silva e Mateus Henrique Machado

'''


#Biblioteca para estabelecimento de conexão entre o cliente e o servidor
import socket

#Função de conversão Celsius -> Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

#Configurações do servidor
host = 'localhost'  # Endereço IP do servidor
port = 55000       # Porta que o servidor irá escutar

#Construção do socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SOCK-STREAM estabelece o protocolo TCP

#Estabelece uma ligaçaõ do socket com uma porta e um host
server_socket.bind((host, port))

#Servidor em modo de escuta (aguardando por uma solicitação)
print("Log - Servidor TCP\nAlunos: Iago Mateus Ávila Fernandes, Lucas Alexsander Barbosa Cruz, Mariano Carlos Silva e Mateus Henrique Machado\n")
server_socket.listen(1)
print(f"Servidor está ouvindo em {host}:{port}")

while True:
    # Aguarda e estabelece a conexão com o cliente
    client_socket, client_address = server_socket.accept()
    print(f"Conexão recebida de {client_address}")

    # Captura a temperatura enviada pelo cliente
    celsius_temp = client_socket.recv(1024).decode()
    print(f"Temperatura em Celsius recebida do cliente: {celsius_temp}°C")

    try:
        # Conversão da temperatura
        fahrenheit_temp = celsius_to_fahrenheit(float(celsius_temp))
        print(f"Temperatura convertida em Fahrenheit: {fahrenheit_temp}°F")

        # Envio da resposta para o cliente
        response = f"Oi cliente, tudo bem? Obrigado pela mensagem. Segue a temperatura convertida em graus Fahrenheit: {fahrenheit_temp}°F"
        client_socket.send(response.encode())
    except ValueError:
        # Caso o input do cliente não seja válido: 
        error_message = "Erro: A temperatura em Celsius deve ser um número válido."
        client_socket.send(error_message.encode())

    # Encerra a conexão com o cliente
    client_socket.close()