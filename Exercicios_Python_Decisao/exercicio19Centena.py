#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas,
# dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#326 = 3 centenas, 2 dezenas e 6 unidades
#12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 
# 10, 21, 11, 1, 7 e 16
# Solicita ao usuário um número inteiro menor que 1000
numero = int(input("Digite um número inteiro menor que 1000: "))

# Verifica se o número está no intervalo válido
if numero >= 0 and numero < 1000:
    # Calcula as centenas, dezenas e unidades
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = (numero % 100) % 10

    # Cria as strings para os termos no plural, se necessário
    centenas_str = f"{centenas} centena" if centenas == 1 else f"{centenas} centenas"
    dezenas_str = f"{dezenas} dezena" if dezenas == 1 else f"{dezenas} dezenas"
    unidades_str = f"{unidades} unidade" if unidades == 1 else f"{unidades} unidades"

    # Imprime o resultado
    if centenas > 0:
        if dezenas > 0 and unidades > 0:
            print(f"{numero} = {centenas_str}, {dezenas_str} e {unidades_str}")
        elif dezenas > 0:
            print(f"{numero} = {centenas_str} e {dezenas_str}")
        elif unidades > 0:
            print(f"{numero} = {centenas_str} e {unidades_str}")
        else:
            print(f"{numero} = {centenas_str}")
    elif dezenas > 0:
        if unidades > 0:
            print(f"{numero} = {dezenas_str} e {unidades_str}")
        else:
            print(f"{numero} = {dezenas_str}")
    elif unidades > 0:
        print(f"{numero} = {unidades_str}")
    else:
        print(f"{numero} = 0")
else:
    print("Número fora do intervalo válido.")