#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a 
#participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser
#classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário,
#ele será classificado como "Inocente".

# Inicializa o contador de respostas afirmativas
respostas_afirmativas = 0

# Realiza as 5 perguntas
pergunta1 = input("Telefonou para a vítima? (Sim ou Não): ")
if pergunta1.lower() == "sim":
    respostas_afirmativas += 1

pergunta2 = input("Esteve no local do crime? (Sim ou Não): ")
if pergunta2.lower() == "sim":
    respostas_afirmativas += 1

pergunta3 = input("Mora perto da vítima? (Sim ou Não): ")
if pergunta3.lower() == "sim":
    respostas_afirmativas += 1

pergunta4 = input("Devia para a vítima? (Sim ou Não): ")
if pergunta4.lower() == "sim":
    respostas_afirmativas += 1

pergunta5 = input("Já trabalhou com a vítima? (Sim ou Não): ")
if pergunta5.lower() == "sim":
    respostas_afirmativas += 1

# Classifica a pessoa com base nas respostas
if respostas_afirmativas == 2:
    print("Você é considerado(a) suspeito(a).")
elif 3 <= respostas_afirmativas <= 4:
    print("Você é considerado(a) cúmplice.")
elif respostas_afirmativas == 5:
    print("Você é considerado(a) assassino(a).")
else:
    print("Você é considerado(a) inocente.")