#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão é sempre pelo mais barato
produto1 = float (input("Digite 1° Numero "))
produto2 = float (input("Digite 2° Numero "))
produto3 = float (input("Digite 3° Numero "))

if produto1<produto2:
    print("Produto n:1° é Menor")
elif produto2<produto3:
    print("Produto n:2° é Menor")
else:
    print("Produto n:3° é Menor")