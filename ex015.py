# Escreva um programa que pergunte a quantidade de Km percorridos por
# um carro alugado e quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado


dias = int(input("Digite por quantos dias o carro foi alugado: "))
km = float(input("Digite quantos KM forma percorridos: "))

valor_dias = dias*60
valor_km = km*0.15
total = valor_dias+valor_km

print("Você ficou com o carro por {} dias e percorreu {}km".format(dias, km))
print("O valor total a pagar é R${:.2f}".format(total))
