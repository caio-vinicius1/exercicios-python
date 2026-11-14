# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# EX: 5! = 5 x 4 x 3 x 2 x 1 = 120
n = int(input('Digite um número: '))
fatorial = 1
contador = n
while contador > 0:
    fatorial *= contador
    print(f'contador = {contador} | fatorial = {fatorial}')
    contador -= 1
print(f'O fatorial de {n} é igual a {fatorial}')

