#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do 
# saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis 
# serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50,
# uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50,
# quatro notas de 10, uma nota de 5 e quatro notas de 1.
# Solicita ao usuário o valor do saque
valor_saque = int(input("Digite o valor do saque (entre 10 e 600 reais): "))

# Verifica se o valor do saque está dentro do intervalo válido
if valor_saque < 10 or valor_saque > 600:
    print("Valor de saque inválido. O valor deve estar entre 10 e 600 reais.")
else:
    # Inicializa as variáveis para contar as notas
    notas100 = notas50 = notas10 = notas5 = notas1 = 0

    # Calcula as notas de 100 reais
    notas100 = valor_saque // 100
    valor_saque %= 100

    # Calcula as notas de 50 reais
    notas50 = valor_saque // 50
    valor_saque %= 50

    # Calcula as notas de 10 reais
    notas10 = valor_saque // 10
    valor_saque %= 10

    # Calcula as notas de 5 reais
    notas5 = valor_saque // 5
    valor_saque %= 5

    # As notas restantes são de 1 real
    notas1 = valor_saque

    # Imprime o resultado
    print(f"Notas de 100 reais: {notas100}")
    print(f"Notas de 50 reais: {notas50}")
    print(f"Notas de 10 reais: {notas10}")
    print(f"Notas de 5 reais: {notas5}")
    print(f"Notas de 1 real: {notas1}")