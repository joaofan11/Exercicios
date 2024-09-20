# 057 Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter uma valor correto.

sexo = str(input('Digite o seu sexo M/F: ')).strip().upper()[0]

while sexo != 'M' and sexo != "F":
    sexo = str(input("Digite o sexo novamente: ")).strip().upper()[0]

print('Seu sexo é {}'.format(sexo))



