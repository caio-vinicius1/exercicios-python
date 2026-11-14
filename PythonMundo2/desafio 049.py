# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, 
# mas agora utilizando um laço for.
from time import sleep
numero = int(input('Digite um número: '))
print('Carregando...')
sleep(1)
for c in range(1,11):
    print(f'{numero} + {c} = {numero + c}')
print('='*10)
for c in range(1,11):
    print(f'{numero} x {c} = {numero * c}')