# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconside-o.
s = 0
pares = []
for c in range(1,7):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
     pares.append(n)
     s += n 
print(f'Os números pares são: {pares}')
print(f'A soma entre os números pares é {s}')
