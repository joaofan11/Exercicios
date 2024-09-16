# 23. Faça um programa que leia um número
# de 0 a 9999 e moste na tela cada um dos digitos separados?


num = int(input("Digite um número: "))
n = str(num)

# print("Utilizando Str:")
# print("Seu número é {}".format(n))
# print("Unidade: {}".format(n[3]))
# print("Dezena: {}".format(n[2]))
# print("centena: {}".format(n[1]))
# print("Milhar: {}".format(n[0]))

print("Utilizando matematica")
print("Seu número é {}".format(n))
print("Unidade: {}".format(num // 1 % 10))
print("Dezena: {}".format(num // 10 % 10))
print("centena: {}".format(num // 100 % 10))
print("Milhar: {}".format(num // 1000 % 10))
