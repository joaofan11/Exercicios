# 054 Crie um programa que leia o ano de nascimento de sete pessoas.
# No final mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0

for pess in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasaceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1

print('São {} pessoas maiores de idade'.format(totalmaior))
print('São {} pessoas menores de idade'.format(totalmenor))
