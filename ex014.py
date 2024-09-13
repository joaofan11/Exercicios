# Escreva um programa que converta uma temperatura digitada em Cº e converta para F°

c = float(input("Digite a temperatura em Celcius: "))

f = ((c*1.8)+32)

print("A empretutra {:.1f}Cº é {:.1f}F".format(c, f))
