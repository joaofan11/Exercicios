# 055 Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e menor peso lidos.

maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input("Digite o peso da {}ª pessoa: ".format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print("O menor peso é {}".format(menor))
print("O maior peso é {}".format(maior))
