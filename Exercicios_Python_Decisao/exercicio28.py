# Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                      Até 5 Kg           Acima de 5 Kg
#File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da 
# promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita 
# no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva
# um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
# contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento,
# valor do desconto e valor a pagar.
# Solicita ao usuário o tipo de carne e a quantidade em Kg
import datetime

# Obter a data e hora da compra
data_hora = datetime.datetime.now()
# Solicita ao usuário o tipo de carne e a quantidade em Kg
tipo_carne = input("Digite o tipo de carne (File Duplo, Alcatra, Picanha): ")
quantidade_kg = float(input("Digite a quantidade em Kg: "))

# Define os preços por Kg
preco_file_duplo = 4.90
preco_alcatra = 5.90
preco_picanha = 6.90

# Verifica o preço com base no tipo de carne
if tipo_carne.lower() == "file duplo":
    preco_kg = preco_file_duplo
elif tipo_carne.lower() == "alcatra":
    preco_kg = preco_alcatra
elif tipo_carne.lower() == "picanha":
    preco_kg = preco_picanha
else:
    print("Tipo de carne inválido.")
    preco_kg = 0.0

# Calcula o valor total da compra
valor_total = quantidade_kg * preco_kg
total = valor_total
# Solicita o tipo de pagamento
tipo_pagamento = input("Digite o tipo de pagamento (Cartão Tabajara sim=s, Outro não=n): ")

# Aplica o desconto de 5% se o pagamento for com o Cartão Tabajara
if tipo_pagamento.lower() == "s":
    desconto = valor_total * 0.05
    valor_total -= desconto

# Imprime o cupom fiscal
print("     Tabajaras Mercados    ")
print("Av: Aparecida, 13 , SP")
print("CNPJ: 00.00.013/0001-13")
print("IE: 000.00000.0013")
print("IM: 000.000/001-3")
print("Data Compra:",data_hora)
print("======CUPOM FISCAL======")
print(f"Tipo de carne: {tipo_carne}")
print(f"Quantidade: {quantidade_kg} Kg")
print(f"Preço por Kg: R$ {preco_kg:.2f}")
print(f"Valor total: R$ {total:.2f}")
print(f"Tipo de pagamento: {tipo_pagamento.capitalize()} Cartão Tabajara")
print(f"Tabajara Desconto: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {valor_total:.2f}")

