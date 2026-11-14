#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$ 7,00 por cada km acima do limite.
from emoji import emojize
velocidade_carro=int(input('Qual foi velocidade do seu carro?: '))
if velocidade_carro<=80:
    print(emojize('Você não ultrapassou o limite de velocidade, PARABÉNS! :smiling_face_with_heart-eyes: '))
else:
    excesso= velocidade_carro-80
    multa=excesso*7.00
    print(emojize(f'Você será multado em: R${multa:.2f} :money_with_wings:'))