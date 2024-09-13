# 11 Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m²

a = float(input("Digite a altura da sua parede: "))
l = float(input("Digite a largura da sua parede: "))

area = a*l

print("A área da sua parede é {}, e você precisa de {}l de tinta para pinta-la".format(area, area/2))
