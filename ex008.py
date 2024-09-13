# 08 Escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros

n1 = float(input("digite um valor em metros: "))

centimetros = float(n1*100)
milimetros = float(n1*1000)

print("O valor convertido em centimetro é {} e milimetros é {}".format(
    centimetros, milimetros))
