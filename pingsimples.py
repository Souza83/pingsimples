import os # Importa o módulo ou bibnlioteca OS (Integra os programas e recursos do SO)


print("#" * 65)  # Imprime o # por 65 veses

ip_ou_host = input("Digite o IP ou Host a ser verificado: ")  # Cria uma variável que recebe do usuário um IP ou Host
print("-" * 65)  # Imprime o - 60 veses
os.system('ping -n 6 {}'.format(ip_ou_host)) # Chamando o system da biblioteca OS, passando o comando ping, número de
# pacotes e a variável informada.
print("-" * 65)  # Imprime o - 60 veses

