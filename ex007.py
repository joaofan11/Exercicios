# 07 Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média

n1 = float(input("Digite a primeira nota do aluno: "))
n2 = float(input("Digite a segunda nota do aluno: "))

media = (n1+n2)/2

print("A média do aluno é {:.1f}".format(media))
