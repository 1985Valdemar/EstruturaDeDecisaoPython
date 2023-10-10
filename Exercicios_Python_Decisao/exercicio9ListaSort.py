#Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = float (input("Digite 1° Numero "))
n2 = float (input("Digite 2° Numero "))
n3 = float (input("Digite 3° Numero "))

#DECRESCENTE
lista = [n1, n2, n3, ]
lista.sort(reverse=True)
print(lista,"Decrescente")

#CRECENTE
listaC = [n1, n2, n3, ]
listaC.sort()
print(listaC,"Crescente")