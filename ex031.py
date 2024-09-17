# 31 Pergunte um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200 Km e R$0,45 para viagens mais longas

distancia = float(input("Qual a distaância da sua viagem: "))

if distancia <= 200:
    print("O valor da sua passagem é {:.2f}".format(distancia*(0.50)))
else:
    print("O valor da sua passagem é {:.2f}".format(distancia*(0.45)))