# Maior e menor
# Leia 6 números inteiros e mostre qual foi o maior e qual foi
#  o menor valor digitado.
maior = 0
menor = 0
for numero in range(1,7):
    n = int(input('Digite um número inteiro: '))
    if numero == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'{maior} é o maior valor')
print(f'{menor} é o menor valor')
