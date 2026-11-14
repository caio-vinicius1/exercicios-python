#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1=int(input('Digite um número: '))
n2=int(input('Digite um número:'))
n3=int(input('Digite um número: '))
if n1>=n2:
    if n1>=n3:
        print(f'{n1} é o maior')
    else:
        print(f'{n3} é o maior')
else:
    if n2>=n3:
        print(f'{n2} é o maior')
    else:
        print(f'{n3} é o maior')

if n1<=n2:
    if n1<=n3:
        print(f'{n1} é o menor')
    else:
        print(f'{n3} é o menor')
else:
    if n2<=n3:
        print(f'{n2} é o menor')
    else:
        print(f'{n3} é o menor')
