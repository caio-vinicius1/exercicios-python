#Desenvolva um programa que pergunte a distância de uma viagem em km.
#Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200 km
#e R$0,45 para viagens mais longas.
distancia_viagem=float(input('Qual foi a distância da viagem em km?: '))
if distancia_viagem<=200:
    passagem_200km=distancia_viagem*0.50
    print(f'A sua viagem ficou no valor de R${passagem_200km:.2f}')
else:
    print('A sua viagem foi longa!')
    viagem_longa=distancia_viagem*0.45
    print(f'Esse é o valor da sua viagem: R${viagem_longa:.2f}')
print('OBRIGADO POR VIAJAR CONOSCO!')

