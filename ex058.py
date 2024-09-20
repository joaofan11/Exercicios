# 058 Melhore o jogo do desafio 028 onde o computador "pensa" em número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.


from random import randint

numeropc = randint(0, 10)
usuario = int(input("tente adivinhar o um número de 0 a 10: "))
c = 0


while numeropc != usuario:
    usuario = int(input("Tente novamente digite um número de 0 a 10: "))
    c += 1

    if numeropc == usuario:
        print("Parabens você acertou")
        print("seu número é {} e o número do pc é {}\n".format(usuario, numeropc))
        print("Você precisou de {} tentativaas para acertar\n".format(c))
    else:
        print("Tente novamente\n")
