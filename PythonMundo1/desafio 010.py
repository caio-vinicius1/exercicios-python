#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.Considere: US$ 1,00= R$3,27
valor=float (input('Qual o valor que você tem em conta?:'))
#quanto vale um dólar em reais
vd= 3.27
dolares= valor / vd
print(f'Com {valor:.2f} reais você pode comprar {dolares:.2f} dólar(es)')
