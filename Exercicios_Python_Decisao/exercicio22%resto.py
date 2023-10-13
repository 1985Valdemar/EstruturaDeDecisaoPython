#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica:
# utilize o operador módulo (resto da divisão).
# Solicita ao usuário um número inteiro
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    print(f"{numero} é um número par.")
else:
    print(f"{numero} é um número ímpar.")