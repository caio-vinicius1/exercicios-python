#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import radians, sin, cos, tan, floor
a= int(input('Digite um ângulo: '))
Converte_radians= radians(a)
sen_1= sin(Converte_radians)
cos_2= cos(Converte_radians)
tan_3= tan(Converte_radians)
print(f'O ângulo de {a}° tem os seguintes valores\nseno:{sen_1:.2f}\ncosseno:{cos_2:.2f}\ntangente:{tan_3:.2f}')
