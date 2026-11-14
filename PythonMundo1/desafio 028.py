#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para...
#o usuario tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuario venceu ou perdeu.
from random import randint
sorteio= randint(0,5)
numero_escolhido=int(input('Tente descobrir qual foi o número inteiro entre 0 e 5, escolhido pelo computador: '))
if sorteio == numero_escolhido:
    print('VOCÊ VENCEU!')
else:
    print('VOCÊ PERDEU!')
print(f'O número escolhido pelo computador é: {sorteio}')