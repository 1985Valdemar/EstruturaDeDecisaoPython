#Faça um Programa que leia um número e exiba o dia correspondente da semana. 
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
# Solicita ao usuário um número correspondente ao dia da semana
numero = int(input("Digite um número (1 a 7) para representar um dia da semana: "))

# Cria um dicionário com os dias da semana
dias_da_semana = {
    1: "Domingo",
    2: "Segunda-feira",
    3: "Terça-feira",
    4: "Quarta-feira",
    5: "Quinta-feira",
    6: "Sexta-feira",
    7: "Sábado"
}

# Verifica se o número está dentro do intervalo válido
if numero >= 1 and numero <= 7:
    # Obtém o nome do dia da semana correspondente
    dia_da_semana = dias_da_semana[numero]
    # Imprime o resultado
    print(f"O número {numero} corresponde a {dia_da_semana}.")
else:
    # Se o número estiver fora do intervalo válido, exibe "Valor inválido"
    print("Valor inválido. Digite um número de 1 a 7 para representar um dia da semana.")