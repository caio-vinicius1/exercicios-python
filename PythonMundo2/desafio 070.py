# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
# perguntar se o usuário vai continuar. No final, mostre:
# Qual é o total gasto na compra.
# Quantos produtos custam mais de R$ 1000.
# Qual é o nome do produto mais barato.
total_compra = 0
valem_mais_demil = 0
produto_barato = ''
menor_preco = 0
contador = 0
while True: 
    nome_produto = str(input('Qual o nome do produto? ').capitalize())
    preco = float(input('Qual o preço do produto? ').replace(',','.'))
    total_compra = total_compra + preco
    contador = contador + 1
    if preco > 1000:
        valem_mais_demil = valem_mais_demil + 1
    if contador == 1 or preco < menor_preco:
        menor_preco = preco
        produto_barato = nome_produto
    usuario = str(input('Você quer continuar? [S/N]: ').upper())
    if usuario == 'N':
        break 
print(f'Total gasto na compra: R$ {total_compra:.2f}'.replace('.',','))
print(f'São {valem_mais_demil} produtos que valem mais de R$1000')
print(f'O produto mais barato é {produto_barato}')
