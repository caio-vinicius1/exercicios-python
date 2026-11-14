#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
nome_cidade= input('Qual o nome da sua cidade?: ').strip()
maiusculo=nome_cidade.upper()
fatiado=maiusculo[0:5]
igual= fatiado == "SANTO"
print(f'O nome da cidade {maiusculo} começa ou não com a palavra SANTO?: {igual}')