#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
# Dica: utilize uma função de arredondamento.
# Solicita ao usuário um número
numero = float(input("Digite um número: "))

# Compara o número original com a sua versão arredondada
#Funcao Round para arrendodar
if numero == round(numero):
    print(f"{numero} é um número inteiro.")
else:
    print(f"{numero} é um número decimal.")