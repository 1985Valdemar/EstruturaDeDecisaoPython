#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular
# a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

Notas1 = float(input("Digite Sua 1° Nota "))
Notas2 = float(input("Digite Sua 2° Nota "))
media = (Notas1+Notas2)/2

if media == 10:
    print("Aprovado com Distincao sua Media é: ",media)
elif media >=7:
    print("Aprovado Sua Media é: ",media)
elif media >=5:
    print("Recuperação",media)
else:
    print("Reprovado",media)