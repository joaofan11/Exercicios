# 28 Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobri qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuario venceu ou perdeu

from random import randint

numeropc = randint(0,5)

usuario = int(input("tente adivinhar o um número de 0 a 5: "))

print("seu número é {} e o número do pc é {}".format(usuario, numeropc))

if numeropc == usuario:
    print("Parabens você acertou")
else:
    print("Tente novamente")


