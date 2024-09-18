# 036 Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ela vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.


casa = float(input("Digite o valor da casa: R$"))
salario = float(input("Digite seu salário: R$"))
anos = int(input("Digite em quantos anos pretende pagar a casa: "))

meses = anos * 12
parcela = casa / meses

condicao = salario * 0.30

if parcela >= condicao:
    print("Emprestimo negado")
else:
    print("Emprestimo aprovado")
