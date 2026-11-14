# EXEMPLO 1:
for c in range(1,10):
    print(c)
print('fim')

# EXEMPLO 2:
c = 1
while c < 10: # while significa 'ENQUANTO'
    print(c)
    c = c + 1
print('Fim')

# EXEMPLO 3:
n = 1
while n != 0: # equanto n for diferente de 0...
    n = int(input('Digite um valor: ')) # faça essa pergunta
print('Fim')  # quando o usuário digitar 0 dá print

# EXEMPLO 4:
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]: ').upper())
print('Fim')

# EXEMPLO 5:
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print(f'Você digitou {par} números pares e {impar} números ímpares!')
