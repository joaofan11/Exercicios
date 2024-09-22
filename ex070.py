# 070 Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar no final,
# mostre: A) Qual o total gasto na compra. B) Quantos produtos custam mais de R$1000 C) qual é o nome do produto mais barato.


soma = menor = maior = contador = 0
nomemenor = ' '

while True:
    print('\n----------Lista de Produtos----------')
    produto = str(input("Digite o produto: "))
    valor = float(input("Digite o valor: R$"))
    continuar = str(
        input("Deseja contniuar sim ou não [S/N]: ")).strip().upper()[0]

    contador += 1
    soma = soma + valor

    if valor > 1000:
        maior += 1

    if contador == 1:
        menor = valor
        nomemenor = produto
    else:
        if valor < menor:
            menor = valor
            nomemenor = produto

    if continuar == 'N':
        break


print(f'\nTotal {soma}')
print(f'Produto de menor valor: {nomemenor}')
print(f'Produtos maiores de R$1000 é: {maior}')
