# 041 A Confederação Nacional da Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#
# Até 9 anos: MIRIM.
# Até 14 anos: Infantil,
# Até 19 anos: Junior,
# Até 20 anos: Sênior,
# Acima: Master.

from datetime import datetime

ano_nascimento = int(input("Digite o ano de nascimento: "))

ano_atual = datetime.now().year

idade = ano_atual - ano_nascimento

if idade <= 9:
    print("Mirim")
elif idade <= 14:
    print("Infantil")
elif idade <= 19:
    print("Junior")
elif idade <= 25:
    print("Sênior")
else:
    print("Master")
