#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros
#vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule
#e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina 
#é R$ 2,50 o preço do litro do álcool é R$ 1,90.
Combustivel = str(input("Digite A-álcool, G-gasolina: "))
Litros = float(input("Quantos Litros: "))

if Combustivel.lower() == "a":
    if Litros <= 20:
        desconto = Litros*0.03
        total = (Litros-desconto)*1.90
        print("seu desconto em Litros: ",desconto,"Total R$: ",Litros*1.90,"Com Desconto R$: ",total)
    elif Litros > 20:
        desconto20 = Litros*0.05
        total20 =(Litros*desconto20)*1.90
        print("seu desconto em Litros: ",desconto20,"Total R$: ",Litros*1.90,"Com Desconto R$: ",total20)
    else:
        print("Erro ao digitar")

elif Combustivel.lower() == "g":
    if Litros <= 20:
        descontogasolina = Litros*0.04
        totalgasolina = (Litros-descontogasolina)*2.50
        print("seu desconto em Litros: ",descontogasolina,"Total R$: ",Litros*2.50,"Com Desconto R$: ",totalgasolina)
    elif Litros >20:
        descontogasolina20 = Litros*0.06
        totalgasolina20 =(Litros*descontogasolina20)*2.50
        print("seu desconto em Litros: ",descontogasolina20,"Total R$: ",Litros*2.50,"Com Desconto R$: ",totalgasolina20)
    else:
         print("Erro ao digitar")
else:
    print("Erro so digitar")