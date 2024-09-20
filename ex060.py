# 060 Faça um programa que leia um número qualquer e mostre seu fatorial.

n = int(input('Digite o número: '))
fatorial = 1
contador = 2

while contador <= n:
 
    fatorial = fatorial * contador
    contador += 1

print(fatorial)
