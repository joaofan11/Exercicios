# 044 Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#
# à vista dinehiro/cheque: 10% de desconto.
# À vista no cartão: 5% de desconto.
# Em até 2x no cartão: preço normal.
# 3x ou mais no cartão: 20% de juros

print("="*50)
valor = float(input("Digite o valor da compra: R$"))
print("="*50)
print('''Digite a opção do seu pagamento 
            1. À vista no dinehiro ou cheque
            2. À vista no cartão
            3. Em até 2x no cartão
            4. 3x ou mais no cartão: ''')
pagamento = int(input('Qual é a opção? '))

print("="*50)

if pagamento == 1:
    print("Seu pagamento teve o desconte de 10% e ficou por R${:.2f}".format(
        valor-(valor*0.10)))
elif pagamento == 2:
    print("Seu pagamento teve o desconto de 5% e ficou por R${:.2f}".format(
        valor-(valor*0.05)))
elif pagamento == 3:
    print("Seu pagamento ficou em R${:.2f}".format(valor))
elif pagamento == 4:
    print("Seu pagamento vai ter um acrecimo de 20% e ficou por R${:.2f}".format(
        valor+(valor*0.2)))
