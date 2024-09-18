# 043 Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela:
#
# Abaixo de 18.5: Abaixo do peso,
# Entre 18.5 e 25: Peso ideal,
# 25 até 30: Sobrepeso,
# 30 até 40: Obesidade,
# Acima de 40: Obesidade mórbida


peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso // (altura*altura)

if imc <= 18.4:
    print("Abaixo do peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso ideal")
elif imc >= 25 and imc <= 30:
    print("Sobre Peso")
elif imc >= 30.1 and imc <= 40:
    print("Obesidade")
elif imc > 40.1:
    print("Obesidade mórbida")
