# Leia 5 números inteiros e mostre a soma deles.
soma = 0
for c in range(5):
   n = int(input('Digite um número inteiro: '))
   soma = soma + n
print(f'A soma equivale a {soma}')
