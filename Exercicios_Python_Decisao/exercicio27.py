#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                      Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
#receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade 
#(em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo
#cliente.
# Solicita ao usuário a quantidade de morangos e maçãs compradas em Kg
quantidade_morangos = float(input("Digite a quantidade de morangos (em Kg): "))
quantidade_macas = float(input("Digite a quantidade de maçãs (em Kg): "))

# Define os preços por Kg
preco_morangos = 2.50  # Até 5 Kg
preco_macas = 1.80  # Até 5 Kg

# Verifica se a quantidade é maior que 5 Kg e aplica o preço correspondente
if quantidade_morangos > 5:
    preco_morangos = 2.20

if quantidade_macas > 5:
    preco_macas = 1.50

# Calcula o valor total da compra
valor_total = (quantidade_morangos * preco_morangos) + (quantidade_macas * preco_macas)

# Verifica se o cliente tem desconto
if quantidade_morangos + quantidade_macas > 8 or valor_total > 25:
    desconto = valor_total * 0.10
    valor_total -= desconto

# Imprime o valor a ser pago pelo cliente
print(f"Valor a ser pago: R$ {valor_total:.2f}")