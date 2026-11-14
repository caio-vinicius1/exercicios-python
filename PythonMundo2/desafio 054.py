# Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final mostre quantas pessoas ainda não atingiram a maioridade 
# e quantas já são maiores.
from datetime import datetime
maioridade = 0
menores = 0
for c in range(1,8,1):
    ano = int(input('Qual o seu ano de nascimento? '))
    idade = datetime.now().year - ano
    if idade >= 18:
        maioridade = maioridade + 1
    else:
        menores = menores + 1 
print(f'{maioridade} pessoas são maiores de idade')
print(f'{menores} pessoas são menores de idade')
