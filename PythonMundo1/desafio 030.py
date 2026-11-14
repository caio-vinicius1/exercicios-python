#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ímPAR.
n_int=int(input('Digite um número inteiro: '))
resto=n_int%2
if resto==0:
    print(f'O número {n_int} é PAR')
else:
    print(f'O número {n_int} é ímPAR')

