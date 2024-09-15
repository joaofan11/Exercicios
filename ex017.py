# Faça um programa que leia o comprimento do cateto oposto e do
# cateto adjacente de um triângulo retângulo, calcule e
# mostre o comprimentoda hipotenusa


# cateto oposto = A
# cateto adjacente = B
# Raiz quadrada de A² + B²

from math import sqrt, hypot

x = float(input("Digite o cateto oposto: "))
y = float(input("Digite o cateto adjacente: "))


hi = hypot(x, y)

# sqrt((x*x)+(y*y))

print("O valor da hipotenusa {:.3f}".format(hi))
