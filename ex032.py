# 32 Faça um programa que leia um ano e mostre se ele é bissexto

ano = int(input("Digite o ano: "))

if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print("Seu ano é bissexto")
else:
    print(("Seu ano não é bissexto"))