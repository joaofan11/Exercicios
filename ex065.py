# 065 Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menos valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores


num = cont = soma = menor = maior = 0
c = 's'

while c in 'Ss':
    num = int(input('Digite um número: '))
    c = str(input('Quer continuar? [S/N] ')).upper().strip()
    cont = cont + 1
    soma = soma + num
    media = soma / cont
    if cont == 1:
        maior = menor = num
    else:
        if  num > maior:
            maior = num
        elif num < menor:
            menor = num
print('Você digitou {} números e a média foi {:.1f}'.format(cont, media))
print('O menor número foi {} e o maior foi {}.'.format(menor, maior))