#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e
# lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
# baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

# Solicita o salário atual do colaborador
salario_atual = float(input("Digite o salário atual do colaborador: R$ "))

# Define as faixas salariais e os percentuais de aumento
faixas_salariais = [280.00, 700.00, 1500.00]
percentuais_aumento = [20, 15, 10, 5]

# Inicializa variáveis para armazenar informações
percentual_aplicado = 0
valor_aumento = 0

# Determina o percentual de aumento com base na faixa salarial
if salario_atual <= faixas_salariais[0]:
    percentual_aplicado = percentuais_aumento[0]
elif salario_atual <= faixas_salariais[1]:
    percentual_aplicado = percentuais_aumento[1]
elif salario_atual <= faixas_salariais[2]:
    percentual_aplicado = percentuais_aumento[2]
else:
    percentual_aplicado = percentuais_aumento[3]

# Calcula o valor do aumento
valor_aumento = (percentual_aplicado / 100) * salario_atual

# Calcula o novo salário
novo_salario = salario_atual + valor_aumento

# Exibe os resultados
print(f"Salário antes do reajuste: R$ {salario_atual:.2f}")
print(f"Percentual de aumento aplicado: {percentual_aplicado}%")
print(f"Valor do aumento: R$ {valor_aumento:.2f}")
print(f"Novo salário após o aumento: R$ {novo_salario:.2f}")