# Crie um programa que faça o computador jogar Jokenpô com você.
# pedra / papel / tesoura
from random import choice
from time import sleep # módulo e função de carregamento...
jogue = str(input('Sua vez: ').upper())
lista = ['pedra','papel','tesoura']
print('Carregando...')
sleep(2) # função de carregamento
computador = choice(lista)
print(f'computador:{computador}')
if jogue == 'pedra' and computador == 'tesoura':
    print(f' VOCÊ VENCEU!')
elif jogue == 'papel' and computador == 'pedra':
    print(f'VOCÊ VENCEU!')
elif jogue == 'tesoura' and computador == 'papel':
    print(f'VOCÊ VENCEU')
elif computador == 'pedra' and jogue == 'tesoura':
    print(f'O COMPUTADOR VENCEU!')
elif computador == 'tesoura' and jogue == 'papel':
    print(f'O COMPUTADOR VENCEU!')
elif computador == 'papel' and jogue == 'pedra':
    print(f'O COMPUTADOR VENCEU!')
else:
    print('EMPATE')