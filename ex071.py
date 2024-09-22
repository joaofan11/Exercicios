# 071 Crie um programa que simule o funcionamento de caixa eletrônico.
# No inicio, pergunte ao usuário qual será o valor a ser sacado (numero inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# Obs: Considerando que o caixa possui cédulas de R$ 50, R%20, RS10 e R$1.


print('='*30)
print("Banco")
print('='*30)

valor = int(input("Qual valor você quer sacar? R$"))
total = valor
ced = 50
totalced = 0

while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
