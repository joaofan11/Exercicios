# 053 Crie um programa que eia uma frase qualquer e diga se lea é um palindromo, desconsiderando os espaços.
# Ex: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA

frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''

for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palindromo')


# print('Você digitou a frase {}'.format(palavras))
