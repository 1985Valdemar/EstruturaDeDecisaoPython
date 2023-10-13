#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele 
# deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.

# Solicita ao usuário dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Pergunta ao usuário qual operação deseja realizar
operacao = input("Escolha a operação (+, -, *, /): ")

# Realiza a operação e calcula o resultado
if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = numero1 - numero2
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        print("Divisão por zero não é permitida.")
        resultado = None
else:
    print("Operação inválida.")
    resultado = None

# Verifica se o resultado é par ou ímpar
par_ou_impar = "par" if resultado % 2 == 0 else "ímpar"

# Verifica se o resultado é positivo ou negativo
positivo_ou_negativo = "positivo" if resultado > 0 else "negativo" if resultado < 0 else "zero"

# Verifica se o resultado é inteiro ou decimal
inteiro_ou_decimal = "inteiro" if resultado.is_integer() else "decimal"

# Imprime o resultado e as informações adicionais
if resultado is not None:
    print(f"O resultado da operação é {resultado}.")
    print(f"É {par_ou_impar}, {positivo_ou_negativo} e {inteiro_ou_decimal}.")