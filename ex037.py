# 037 Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1. binário 2. octal 3. hexadecimal


num = int(input("Digite um número inteiro: "))
print('''Esolha uma das bases para conversão:
      [1] Binario
      [2] Octal
      [3] Hexadecimal''')
opcao = int(input("Sua opção: "))

if opcao == 1:
    print("{} convertido para BINARIO é {}".format(num, bin(num)[2:]))
elif opcao == 2:
    print("{} convertido para OCTAL é {}".format(num, oct(num)[2:]))
elif opcao == 3:
    print("{} convertido para HEXADECIMAL é {}".format(num, hex(num)[2:]))
else:
    print("Opção invalida. Tente novamente")
