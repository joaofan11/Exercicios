# 049 Refaça o desafio 09, mostrando a tabuada de um número que o usuário escolher, utilizando um laço for.

numero = int(input("Digite um número: "))

for c in range(1, 11):
    print("{} * {:2} = {:2}".format(numero, c, numero*c))
