# 35 Desenvolva um programa que leia o comprimento de três retas e diga se elas podem ou não formar um triângulo

r1 = float(input("Digite o tamanho da primeira reta: "))
r2 = float(input("Digite o tamanho da segunda reta: "))
r3 = float(input("Digite o tamanho da terceira reta: "))

if r1 < (r2+r3) and r2 < (r1+r3) and r3 < (r1+r2):
    print("Seu triangulo exite")
else:
    print("Seu triangulo não existe")
