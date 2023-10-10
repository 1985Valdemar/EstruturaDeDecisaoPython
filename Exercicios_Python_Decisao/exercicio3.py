#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra
# escrever: F - Feminino, M - Masculino, Sexo Inválido
n1 = str(input("Digite seu sexo M = Masculino ou  F = Feminino "))
if  n1 == "M":
    print("Sexo Masculino")
elif n1 == "F":
    print("Sexo Feminino")
else:
    print("Erro na letra")
    
  