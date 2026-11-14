# Crie um programa que leia vários números inteiros pelo teclado.
#  No final da execução, mostre a média entre todos os valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar 
# a digitar valores.
n1 = int(input('Digite um número inteiro pelo teclado: '))
usuario = str(input('Você quer continuar a digitar números? [S/N]: ').upper())
soma = n1
c = 1
while usuario != 'N':
    n = int(input('Digite um número inteiro pelo teclado: '))
    c = c + 1
    soma = soma + n
    usuario = str(input('Você quer continuar a digitar números? [S/N]: ').upper())
media = soma / c
print(f'A média entre todos os valores lidos é: {media}')
print(f'Números lidos: {c}, média: {media}!')
