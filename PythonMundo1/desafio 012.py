#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
#Conversão feita
preco= float(input('Qual o valor do produto?:'))
d= preco*0.05
print(d)
print(f'O valor do produto com 5% de desconto é:R${preco-d:.2f}')