# 062 Melhore o desafio 61, perguntando para o usuário se ele quer mostra mais alguns termos.
# O programa encerra quando ele disser que quer mostra 0 termos.

primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
termo = primeiro
c = 1
total = 0
mais = 10


while mais != 0:
    total = total + mais
    while c <= total:
        print('{} - '.format(termo), end='')
        termo += razao
        c += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais: "))
print('fim')
