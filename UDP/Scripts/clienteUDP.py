'''
Redes de Computadores II - Trabalho 2 

Script Cliente UDP

Alunos: Iago Mateus Ávila Fernandes, Lucas Alexsander Barbosa Cruz, Mariano Carlos Silva e Mateus Henrique Machado

'''


#Biblioteca para estabelecimento de conexão entre o cliente e o servidor
import socket

# Configurações do servidor
host = 'localhost'  # Endereço IP do servidor
port = 55000        # Porta que o servidor está escutando

# Construção do socket do cliente 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #SOCK_DGRAM usado para estabelecer o protocolo UDP


print("Log - Cliente TCP\nAlunos: Iago Mateus Ávila Fernandes, Lucas Alexsander Barbosa Cruz, Mariano Carlos Silva e Mateus Henrique Machado\n")

# Espera pelo input da temperatura do cliente
celsius_temp = input("Digite a temperatura em Celsius: ")

# Envio da temperatura para o servidor
client_socket.sendto(celsius_temp.encode(), (host, port))

# Captura da resposta do servidor
response, server_address = client_socket.recvfrom(1024)
print(f"Resposta do servidor: {response.decode()}")

# Encerra o socket do cliente
client_socket.close()
