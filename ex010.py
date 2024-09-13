# 10 Crie um programa que leia quanto dinehiro uma pessoa tem na carteira e mostre quantos dólares ela pode compra (considere US$ 1.00 = R$ 3,27)

n1 = float(input("Quantos reais você tem na carteira: "))

print("O valor convertido em dolares é {:.2f}".format(n1/3.27))
