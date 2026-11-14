# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar
# mais alguns termos. O programa encerra quando ele disser quer quer
# mostrar os termos.
primeiro_termo = int(input('Digite o primeiro termo da progressão: '))
r = int(input('Digite a razão da progressão: '))
c = 0
while c < 10:
    termo = primeiro_termo + (c * r)
    print(termo)
    c += 1
print('Ao digitar 0 o programa encerra')
usuario = int(input('Quantos termos a mais você quer ver? '))
while usuario != 0:
    total = c + usuario
    while c < total:
        termo = primeiro_termo + (c * r)
        print(termo)
        c += 1
    usuario = int(input('Quantos termos a mais você quer ver? '))
print('Fim')

