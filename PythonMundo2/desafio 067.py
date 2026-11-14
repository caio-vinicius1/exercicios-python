# Faça um programa que mostre a tabuada de varios números, um de cada vez, para cada valor
# digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
c = 1
while True:
    n = int(input('Digite um número (número negativo encerra): '))
    if n < 0:
        break
    for c in range (1, 11):
        print(f'{n} + {c} = {n + c}')
    print('=' *10)
    for c in range (1, 11):
        print(f'{n} - {c} = {n - c}')
    print('=' *10)
    for c in range (1, 11):
        print(f'{n} x {c} = {n * c}')
    print('=' * 10)
    for c in range (1, 11):
        print(f'{n} : {c} = {n // c}')
    print('=' *10)
    c = c + 1
print('Encerrado')
