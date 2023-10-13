#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
from datetime import datetime

def validar_data(data_texto):
    try:
        # Tente criar um objeto datetime com a data fornecida
        datetime.strptime(data_texto, '%d/%m/%Y')
        return True
    except ValueError:
        return False

# Solicita ao usuário uma data
data_digitada = input("Digite uma data no formato dd/mm/yyyy: ")

# Verifica se a data é válida
if validar_data(data_digitada):
    print("A data é válida.")
else:
    print("A data não é válida.")