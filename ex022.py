# 22. Crie um programa que leia o nome completo de uma pessoa e mostre:

# 1. O nome com todas as letras maisculas
# 2. O nome com todas letras minusculas
# 3. Quantas letras ao todo (Sem considerar espaços)
# 4. Quantas letras tem o primeiro nome


nome = input("Digite se nome completo: ")

print("Seu nome em maiúsculas é {}".format(nome.upper()))
print("Seu nome em minúsculas é {}".format(nome.lower()))

print("Sem nome tem ao todo {} letras ".format(len(nome.replace(" ", ""))))
print("Seu primeiro nome é {}".format(nome.split()[0]))
print("Seu primeiro nome tem {} letras".format(len(nome.split()[0])))
