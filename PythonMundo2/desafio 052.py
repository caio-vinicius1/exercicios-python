# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('Digite um número inteiro: '))
if n <= 1:
    print('O número NÃO É PRIMO')
else:
    ninguem_dividiu_ainda = 0
    for c in range(2, n):
        if n % c == 0:
         ninguem_dividiu_ainda = ninguem_dividiu_ainda + 1
    if ninguem_dividiu_ainda == 0:
        print('Nínguém dividiu, então o número é PRIMO')
    else:
        print('Alguém dividiu, então o número NÃO É PRIMO')
