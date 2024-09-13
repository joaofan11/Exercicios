# Exercício Python 004: Faça um programa que leia algo pelo
# teclado e mostre na tela o seu tipo primitivo e todas as
# informações possíveis sobre ele.

n = input('Digite qualquer coisa: ')

print("O tipo primitio desse valor é ", type(n))
print("É um número? ", n.isnumeric())
print("Só tem espaços? ", n.isspace())
print("É um alfavético? ", n.isalpha())
print("É alfanomérico? ", n.isalnum())
print("Está em maiúsculas? ", n.isupper())
print("Está em minúsculas? ", n.islower())
print("Está capitalizada? ", n.istitle())
