# 26. Faça um programa que leia uma frase pelo teclado e mostre

# 1. Quatas vezes aparece a letra "A"
# 2. Em que posição ela aparece a primeira vez
# 3. Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper()

print('A letra A aparec {} vezes'.format(frase.count('A')))
print('A primeira letra A apare na posição {}'.format(frase.find('A')+1))
print('A última letra A apare na posição {}'.format(frase.rfind('A')+1))
