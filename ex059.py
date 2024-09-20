# 059 Crie um programa que leia 2 valores e mostre um menu na tela:
# [1] somar [2]multiplicar [3]maior [4]Novos números [5]Sair do programa.
# Seu programa deverá realizar a operação em cada caso.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número "))
opcao = 0

while opcao != 5:
    opcao = int(input(
        'Digite a opção que deseja: [1] Somar [2] Multiplicar [3] Maior [4] Novos números [5] Sair do programa: '))
    if opcao == 1:
        print("A soma de {} e {} é {}".format(n1, n2, (n1+n2)))
    elif opcao == 2:
        print("A multiplicação de {} e {} é {}".format(n1, n2, (n1*n2)))
    elif opcao == 3:
        if n1 > n2:
            print("O maior número entre {} e {} é {}".format(n1, n2, n1))
        else:
            print("O maior valor entre {} e {} é {}".format(n1, n2, n2))
    if opcao == 4:

        n1 = int(input('Digite o primeiro número novamente: '))
        n2 = int(input('Digite o segundo número novamente: '))

print("Saiu do programa")
