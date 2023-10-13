import datetime

# Obter a data e hora da compra
data_hora = datetime.datetime.now()

# Solicitar ao usuário o tipo e a quantidade de carne comprada
tipo_carne = input("Qual é o tipo de carne que você comprou? ")
quantidade = float(input("Quantos quilos de carne você comprou? "))

# Calcular o preço total da compra
if quantidade <= 5:
    if tipo_carne == "File Duplo":
        preco_total = quantidade * 4.9
    elif tipo_carne == "Alcatra":
        preco_total = quantidade * 5.9
    elif tipo_carne == "Picanha":
        preco_total = quantidade * 6.9
else:
    if tipo_carne == "File Duplo":
        preco_total = quantidade * 5.8
    elif tipo_carne == "Alcatra":
        preco_total = quantidade * 6.8
    elif tipo_carne == "Picanha":
        preco_total = quantidade * 7.8

# Aplicar o desconto de 5% se o pagamento for feito com o cartão Tabajara
pagamento = input("Você vai pagar com o cartão Tabajara? (sim/não) ")
if pagamento == "sim":
    desconto = preco_total * 0.05
else:
    desconto = 0

# Calcular o valor a pagar
valor_a_pagar = preco_total - desconto

# Imprimir as informações da compra em um cupom fiscal
print("========== CUPOM FISCAL ==========")
print("Data e hora da compra:", data_hora)
print("Tipo de carne:", tipo_carne)
print("Quantidade:", quantidade, "kg")
print("Preço total: R$", preco_total)
print("Tipo de pagamento:", pagamento)
print("Valor do desconto: R$", desconto)
print("Valor a pagar: R$", valor_a_pagar)