#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
Qkm= float(input('Qual a quantidade de km rodado pelo carro alugado?:'))
Qdi= int(input('Quantos dias o carro foi alugado?:'))
c= Qkm*0.15
c1= Qdi*60
print(f'Total a pagar R${c+c1:.2f}')