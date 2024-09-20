# 064 Crie um programa que leia vários numero inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#
# No final mostres quantos número foram digitados e qual foi a soma entre eles (desconsiderando o 999)

n = 0
c = 0
soma = 0

while n != 999:
    n = int(input("Digite o número [999 para parar]: "))
    c += 1
    soma = soma+n

print("Você digitiou {} vezes e a soma é {}".format((c-1), (soma-999)))
