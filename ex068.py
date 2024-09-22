# 068 Faça um programa que jogue par ou impa com o computador.
# O jogo será interrompido quando o jogador perder, mostrando o total de vitorias consecutivas que ele conquistou no final do jogo

from random import randint

soma = c = 0

while True:
    print("-="*20)
    print("Vamos jogar PAR ou ÍMPAR")
    print("-="*20)

    user = int(input("Diga um valor de 0 a 10: "))
    pc = randint(0, 10)
    soma = user+pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input("Par ou Impar? [P/I]: ")).strip().upper()[0]
    print(f"VocÊ jogou {user} e o computador jogou {pc}")

    if tipo == 'P':
        if soma % 2 == 0:
            print("Você venceu")
            c += 1
        else:
            print("Você perdeu")
            break
    elif tipo == "I":
        if soma % 2 != 0:
            print("Você venceu")
            c += 1
        else:
            print("Você perdeu")
            break

    print("Vamos jogar novamente ")
print(f"Acabou você venceu {c}")
