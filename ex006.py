# 06 Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n1 = int(input("Digite um número: "))

d = n1+n1
t = n1+n1+n1
r = n1**(1/2)

print("O dobro do seu número é {}, o triplo é {} e a raiz quadrada é {:.2f}".format(d, t, r))
