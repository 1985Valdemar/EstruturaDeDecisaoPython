# Solicita ao usuário as duas notas parciais
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Calcula a média das notas
media = (nota1 + nota2) / 2

# Determina o conceito com base na média
if media >= 9.0 and media <= 10.0:
    conceito = "A"
elif media >= 7.5 and media < 9.0:
    conceito = "B"
elif media >= 6.0 and media < 7.5:
    conceito = "C"
elif media >= 4.0 and media < 6.0:
    conceito = "D"
else:
    conceito = "E"

# Imprime as notas, a média e o conceito
print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Média: {media}")
print(f"Conceito: {conceito}")

# Determina se o aluno foi aprovado ou reprovado
if conceito in ["A", "B", "C"]:
    print("APROVADO")
else:
    print("REPROVADO")