# 067 Faça um programa que mostre a tabuada de vários número, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.


while True:
    n = int(input("Que ver a tabuada de qual valor? "))

    if n < 0:
        print('Fim do programa')
        break
    for c in range(1, 11):
        print(f'{n} * {c} = {c*n}')
    print('-'*20)
