# 040 Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#
# Média até de 4.9: REPROVADO,
# Média entre 5.0 e 6.9: Recuperação,
# Média 7.0 ou superior: APROVADO

n1 = float(input("Digite a preimeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2)//2

if media <= 4.9:
    print("Reprovado")

elif media >= 5 and media <= 6.9:
    print("Recuperação")
else:
    print("Aprovado")
