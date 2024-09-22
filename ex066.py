# 066 Crie um programa que leia vários número inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsidere a flag)


contador = soma = 0

while True:
    n = int(input("Digite um número (999 parar): "))
    if n == 999:
        break
    contador += 1
    soma = soma+n

print(f'Você digitou {contador} vezes e a soma é {soma}')
