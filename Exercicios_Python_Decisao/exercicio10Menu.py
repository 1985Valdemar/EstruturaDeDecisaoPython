#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino
# ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", 
# conforme o caso.
while True:
    # Exibe as opções do menu para o usuário
    print("Menu:")
    print("M. Opção Matutino M")
    print("V. Opção Vespertino V")
    print("N. Opção Noite N")
    print("S. Sair")
    
    # Solicita ao usuário que escolha uma opção
    escolha = input("Escolha uma opção (M/V/N/S): ")
    
    # Verifica a escolha do usuário e executa a ação correspondente
    if escolha == "M":
        print("Você escolheu a Opção M-matutino.")
        # Coloque aqui o código para a Opção M-matutino
    elif escolha == "V":
        print("Você escolheu a Opção V-Vespertino.")
        # Coloque aqui o código para a Opção V-Vespertino
    elif escolha == "N":
        print("Você escolheu a Opção  N-Noturno.")
        # Coloque aqui o código para a Opção N-Noturno
    elif escolha == "S":
        print("Saindo do programa. Adeus!")
        break  # Sai do loop e encerra o programa
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        # Mensagem de Falha ao digitar Numero que não seja da lista ou minusculo