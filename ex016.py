# Crie um programa que leia um número real qualquer pleo tecaldo
# e mostre na tela su porção inteira. Ex: Digite um númeto: 6.127. O número 6.127 tem a parte inteira 6.


from math import trunc


num = float(input("Digite um valor: "))

print("o valor digitado é: {} e o valor inteiro dele é {}".format(num, trunc(num)))
