#Faça um Programa que leia três números e mostre o maior e o menor deles.
n1 = float (input("Digite 1° Numero "))
n2 = float (input("Digite 2° Numero "))
n3 = float (input("Digite 3° Numero "))

if n1 > n2:
    print("Numero 1° é Maior")
elif n2 > n3:
    print("Numero 2° é Maior")
else:
    print("Numero 3° é Maior")
if n1<n2:
    print("Numero 1° é Menor")
elif n2<n3:
    print("NUmero 2° é Menor")
else:
    print("Numero 3° é Menor")