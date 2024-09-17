# 34 Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para Os inferiores ou iguais, o aumento é de 15%

salario = float(input("Digite o sálario: "))

if salario <= 1250.00:
    print("Seu aumento é de {:.2f}".format(salario*0.15))
else:
    print("Seu aumento é de {:.2f}".format(salario*0.10))