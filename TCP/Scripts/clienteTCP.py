'''
Redes de Computadores II - Trabalho 2 

Script Cliente TCP

Alunos: Iago Mateus Ávila Fernandes, Lucas Alexsander Barbosa Cruz, Mariano Carlos Silva e Mateus Henrique Machado

'''


# Biblioteca para estabelecimento de conexão entre o cliente e o servidor
import socket

# Configurações do cliente
host = 'localhost'  # Endereço IP do servidor
port = 55000       # Porta do servidor

# Construção do socket do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SOCK_STREAM indica a conexão TCP

# Conexão com o servidor com os parãmetros do cliente e a porta que será utilizada
client_socket.connect((host, port))

print("Log - cliente TCP\nAlunos: Iago Mateus Ávila Fernandes, Lucas Alexsander Barbosa Cruz, Mariano Carlos Silva e Mateus Henrique Machado\n")

# Espera pelo input da temperatura do cliente
celsius_temp = input("Digite a temperatura em Celsius: ")

# Envio da temperatura para o servidor
client_socket.send(celsius_temp.encode())

# Captura da resposta do servidor 
response = client_socket.recv(1024).decode()
print(f"Resposta do servidor: {response}")

# Encerramento da conexão com o servidor
client_socket.close()