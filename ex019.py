# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles a escrevendo o nome do escolhido.

from random import choice

nome1 = str(input("Digite o primeiro nome: "))
nome2 = str(input("Digite o segundo nome: "))
nome3 = str(input("Digite o terceiro nome: "))
nome4 = str(input("Digite o quarto nome: "))
lista = [nome1, nome2, nome3, nome4]

escolhido = choice(lista)

print("O aluno escolhido foi {}".format(escolhido))
