# 042 Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#
# Equilátero: todos os lados são iguais,
# Isósceles: dois lados iguais.
# Escaleno: todos os lados diferentes


r1 = float(input("Digite o tamanho da primeira reta: "))
r2 = float(input("Digite o tamanho da segunda reta: "))
r3 = float(input("Digite o tamanho da terceira reta: "))


if r1 < (r2+r3) and r2 < (r1+r3) and r3 < (r1+r2):
    print("Seu triangulo é ", end='')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓCELES')

else:
    print("Seu triangulo não existe")
