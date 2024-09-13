# 13 Faça um algoritmo que leua o salário de um funcionario e mostre seu novo salário, com 15% de aumento.

n = float(input("Digite seu salário: "))

aumento = n+(n*0.15)

print("O salario com 15% de aumento é: {:.2f}".format(aumento))
