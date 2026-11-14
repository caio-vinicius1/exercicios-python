# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
print('Cadastro de pessoas')
pessoas_mais18 = 0
homens = 0
mulheres_menos20 = 0
while True:
    idade = int(input('Qual a sua idade? '))
    sexo = str(input('Qual seu sexo? [M/F]: ').upper())
    if idade >= 18:
        pessoas_mais18 = pessoas_mais18 + 1
    if sexo == 'M':
        homens = homens + 1
    elif sexo == 'F' and idade < 20:
        mulheres_menos20 = mulheres_menos20 + 1
    continuar = str(input('Você quer continuar? [S/N]: ').upper())
    if continuar == 'N':
        break
print('=><' * 24)
print(f'Pessoas com mais de 18 anos {pessoas_mais18}')
print(f'Homens cadastrados {homens}')
print(f'Mulheres com menos de 20 anos {mulheres_menos20}')
