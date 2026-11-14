# Crie um programa  que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição
# de parada. No final, mostre quantos números foram digitados e qual foi a soma
# entre eles (desconsiderando o flag).
n_digitados = 0
soma = 0
while True:
    n = int(input('Digite um número inteiro: '))
    if n == 999:
        break
    n_digitados = n_digitados + 1
    soma = soma + n
print(f'Foram {n_digitados} número(s) digitado(s)')
print(f'A soma dos números é {soma}')
