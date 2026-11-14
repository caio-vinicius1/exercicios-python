# Faça um programa que leia o peso de 5 pessoas. No final, 
# mostre qual foi o maior e o menor peso lidos.
maior_peso = 0
menor_peso = 1000
for _ in range(1,6,1):
    peso = float(input('Qual o seu peso em (kg): '))
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso
print(f'maior peso: {maior_peso}, menor peso: {menor_peso}')