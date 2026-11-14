# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa mostre:
# - A média de idade do grupo
# - Qual é o nome do homem mais velho 
# - Quantas mulheres têm menos de 20 anos.

# --- Variáveis iniciais (as "gavetas") ---
volta = 0
soma_das_idades = 0 # vai acumular as idades de todo mundo.
maior_idade_entre_homens = 0 # Guarda o “recorde” de idade entre os homens. Começa em zero para que o primeiro homem sempre ganhe dele.
nome_do_homem_mais_velho = ""  # Guarda o nome de quem tem o recorde. Começa como texto vazio.
mulheres_com_menos_de_vinte = 0 # contador de mulheres com menos de 20 anos.
# Laço de repetição com for
for c in range(1,5,1):
    print(f'Pessoa {c}') # Para classificar as pessos com número: pessoa1...
    nome = str(input('Qual o seu nome? '))
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Qual seu sexo? ').upper())
    soma_das_idades += idade
    if sexo == 'masculino'.upper() and idade > maior_idade_entre_homens:
        maior_idade_entre_homens = idade
        nome_do_homem_mais_velho = nome
    if sexo == 'feminino'.upper() and idade < 20:
        mulheres_com_menos_de_vinte += 1
media = soma_das_idades / 4
print('>'*20)
print(f'A média das idades é {media}')
print(f'nome do homem mais velho é {nome_do_homem_mais_velho}')
print(f'São {mulheres_com_menos_de_vinte}  mulheres com menos de 20 anos')
