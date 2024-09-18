# 045 Crie um programa que faça o computador Pedra, Papel e Tesoura com você.


from random import randint

pc = randint(1, 3)
use = int(input("Jogue 1.Pedra, 2.Papel, 3.Tesoura: "))

######################################################
if use == 1:
    print("Você escolheu Pedra\n")
elif use == 2:
    print("Você escolheu Papel\n")
else:
    print("Você escolheu Tesoura\n")
######################################################
if pc == 1:
    print("O pc escolheu Pedra\n")
elif pc == 2:
    print("O pc escolheu Papel\n")
else:
    print("O pc escolheu Tesoura\n")
######################################################
if pc == use:
    print("O jogo empatou\n")

elif pc == 1 and use == 3:
    print("O PC ganhou\n")
elif pc == 2 and use == 1:
    print("O PC ganhou\n")
elif pc == 3 and use == 2:
    print("O PC ganhou\n")

elif use == 1 and pc == 3:
    print("Você ganhou\n")
elif use == 2 and pc == 1:
    print("Você ganhou\n")
elif use == 3 and pc == 2:
    print("Você ganhou\n")
