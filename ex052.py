# 052 Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input("Digite um número: "))

if n <= 1:
    print('O número não é primo')
for c in range(2, n):
    if n % c == 0:
        print('O número não é primo')
    else:
        print("O número é primo")
