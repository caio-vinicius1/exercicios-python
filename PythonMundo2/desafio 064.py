# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números
# foram digitados e qual foi a soma entre eles (desconsiderando o flag(999)).
print('Digito de parada: [999]')
n = int(input('Digite um número inteiro: '))
c = 0
soma_total = 0
while n != 999:
    c = c + 1
    soma_total = soma_total + n
    n = int(input('Digite um número inteiro: '))
if c == 0:
    print(f'Não há soma, números digitados: {c}')
else:
    print(f'Soma: {soma_total}, números digitados: {c}')
