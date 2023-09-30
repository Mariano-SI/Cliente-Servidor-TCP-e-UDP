'''
Redes de Computadores II - Trabalho 2 

Script Servidor UDP

Alunos: Iago Mateus Ávila Fernandes, Lucas Alexsander Barbosa Cruz, Mariano Carlos Silva e Mateus Henrique Machado

'''


#Biblioteca para estabelecimento de conexão entre o cliente e o servidor
import socket

#Função de conversão Celsius -> Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Configurações do servidor
host = 'localhost'  # Endereço IP do servidor
port = 55000        # Porta que o servidor irá escutar

# Cria o socket do servidor usando UDP (SOCK_DGRAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #SOCK_DGRAM usado para estabelecer o protocolo UDP

#Estabelece uma ligaçaõ do socket com uma porta e um host
server_socket.bind((host, port))

print("Log - Servidor UDP\nAlunos: Iago Mateus Ávila Fernandes, Lucas Alexsander Barbosa Cruz, Mariano Carlos Silva e Mateus Henrique Machado\n")

print(f"Servidor está ouvindo em {host}:{port}")

while True:
    # Aguarda a conexão do cliente e recebe uma solicitação
    celsius_temp, client_address = server_socket.recvfrom(1024)
    celsius_temp = celsius_temp.decode()
    print(f"Temperatura em Celsius recebida do cliente: {celsius_temp}°C")

    try:
        # Conversão da temperatura
        fahrenheit_temp = celsius_to_fahrenheit(float(celsius_temp))
        print(f"Temperatura convertida em Fahrenheit: {fahrenheit_temp}°F")

        # Envio da resposta para o cliente
        response = f"Oi cliente, tudo bem? Obrigado pela mensagem. Segue a temperatura convertida em graus Fahrenheit: {fahrenheit_temp}°F"
        server_socket.sendto(response.encode(), client_address)
    except ValueError:
        # Caso o input do cliente seja inválido
        error_message = "Erro: A temperatura em Celsius deve ser um número válido."
        server_socket.sendto(error_message.encode(), client_address)
