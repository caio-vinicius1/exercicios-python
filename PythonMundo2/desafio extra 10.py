#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre:
# quantos números foram lidos;
# o maior e o menor valor digitado;
# a soma apenas dos números pares.
n = int(input('Digite um número inteiro: '))
c = 1
menor = 0
maior = 0
soma = 0
while n != 0:
    n = int(input('Digite um número inteiro: '))
    c = c + 1
    if n < menor:
        menor = menor + n
    elif n > maior:
        maior = maior + n
    elif n % 2 == 0:
        soma = soma + n
print(f'Foram lido {c} número(s)')
print(f'{soma} é a soma dos números pares')
print(f'{menor} é o menor valor')
print(f'{maior} é o maior valor')
print('fim')
