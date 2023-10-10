#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo
# de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  #Média de Aproveitamento  Conceito
  #Entre 9.0 e 10.0        A
  #Entre 7.5 e 9.0         B
  #Entre 6.0 e 7.5         C
  #Entre 4.0 e 6.0         D
  #Entre 4.0 e zero        E
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem
# “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
Nota1 = float(input("Digite Sua 1° Nota "))
Nota2 = float(input("Digite Sua 2° Nota "))
media = (Nota1+Nota2)/2
print("Sua 1° Nota: ",Nota1)
print("Sua 2° Nota: ",Nota2)
if media >= 9:
    print("Sua Media é: ",media,",Conceito: A",",Está Aprovado")
elif media >= 7.5:
    print("Sua Media é: ",media,",Conceito: B",",Está Aprovado")
elif media >= 6:
    print("Sua Media é: ",media,",Conceito: C",",Está Aprovado")
elif media >= 4:
    print("Sua Media é: ",media,",Conceito: D",",Está Reprovado")
else:
    print("Sua Media é: ",media,",Conceito: E",",Está Reprovado")