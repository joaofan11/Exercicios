# 056 Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# A média de idade do grupo.
# Qual é o nome do homem maís velho.
# Quantas mulheres tem mesnos de 20 anos.

somaidade = 0
media = 0
maioridadehomem = 0
nomevelho = 0
totmulher20 = 0

for c in range(1, 5):
    print("============= {}ª PESSOA =============".format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): '))
    somaidade += idade

    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1


media = (somaidade/4)
print('A média de idades é {}'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(
    maioridadehomem, nomevelho))
print('Ao todo são {} mulheres abaixo dos 20 anos'.format(totmulher20))
