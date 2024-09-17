# 29 Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input("Digite a sua velocidade: "))
multa = velocidade - 80.00

if velocidade > 80.00:
    print("O valor da sua multa é: {:.1f}".format(multa*7))

else:
    print("Limite dentro do permitido")