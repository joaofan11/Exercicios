# 069 Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programam deverá perguntar se o usuário quer ou não continuar.
# No final, mostre: A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos.

totalHomem = total18 = totalM20 = 0

while True:
    print('\n----------Cadastro de pessoas----------')
    sexo = str(input("Digite o sexo [M/F]: ")).strip().upper()[0]
    idade = int(input("Digite a idade: "))
    continuar = str(
        input("Deseja contniuar sim ou não [S/N]: ")).strip().upper()[0]

    if idade > 18:
        total18 += 1

    if sexo == 'M':
        totalHomem += 1

    if sexo == 'F':
        totalM20 += 1

    if continuar == 'N':
        break

print(f'\nTotal de homens cadastrados: {totalHomem}')
print(f'Foram de pessoas maiores de 18 anos: {total18}')
print(f'Total de mulheres maiores de 20 anos: {totalM20}')
