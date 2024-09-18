# 039 Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo.

from datetime import datetime

ano_nascimento = int(input("Digite seu ano de nascimento: "))

ano_atual = datetime.now().year

anos = ano_atual - ano_nascimento

if anos < 18:

    print("Ainda não é preciso se alistar")
    print("Ainda falta {} anos para se alistar".format((-1)*(anos-18)))

elif anos == 18:

    print("Está na hora de se alistar")

elif anos >= 19:

    print("Já passou do tempo de alistamento")
    print("Já passou {} anos do seu alistamento".format(anos-18))
