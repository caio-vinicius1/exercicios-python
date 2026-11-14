# Exercício: Cadastro de Alunos
# Desenvolva um programa que leia o nome, a nota final e o sexo de 5 alunos.
#No final do programa, mostre:

# A média das notas da turma
# O nome da aluna com a maior nota (entre as mulheres)
# Quantos homens tiraram nota abaixo de 6
media = 0
maiornota_aluna = 0
nome_da_aluna = ''
homem_nota_abaixode_seis = 0
for i in range(1,6):
    print(f'{i}° aluno(a):')
    nome = str(input('Digite seu nome: ').upper())
    nota_final = float(input('Digite a nota final: '))
    media = media + nota_final
    sexo = str(input('Qual seu sexo? ').upper())
    if sexo == 'F' and nota_final > maiornota_aluna :
        nome_da_aluna = nome
        maiornota_aluna = nota_final
    elif sexo == 'M' and nota_final < 6:
        homem_nota_abaixode_seis = homem_nota_abaixode_seis + 1
print(f'A média das notas dos alunos é: {media / 5:.1f}')
print(f'O nome da aluna com a maior nota é {nome_da_aluna}, com a nota: {maiornota_aluna}')
print(f'{homem_nota_abaixode_seis} homem(s) com a nota abaixo de 6')
