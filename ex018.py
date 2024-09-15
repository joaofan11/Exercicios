# Faça um programa que leia um ângulo qualquer e mostre na tela o
# seno, cosseno e a tangente desse angulo

from math import radians, sin, cos, tan

ang = int(input("Digite um ângulo: "))

# Para fazer a conversão é necessario que o angulo esteja em radianos

rad = radians(ang)

print("O seno de {}º é {:.2}".format(ang, sin(rad)))
print("O cosseno de {}º é {:.2}".format(ang, cos(rad)))
print("A tangente de {}º é {:.2}".format(ang, tan(rad)))
