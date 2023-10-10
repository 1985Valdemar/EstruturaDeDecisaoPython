#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
# Solicita que o usuário digite uma letra
letra = input("Digite uma letra: ")

# Verifica se a entrada é uma única letra
if len(letra) == 1:
    # Converte a letra para minúscula para facilitar a comparação
    letra = letra.lower()
    
    # Verifica se a letra é uma vogal
    if letra in "aeiou":
        print("É uma vogal.")
    else:
        print("É uma consoante.")
else:
    print("Por favor, digite apenas uma única letra.")