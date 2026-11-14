#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Exe: Digite um número: 6.127
#O número 6.127 tem a parte Inteira 6.
from math import trunc
Nr= float(input('Digite um número: '))
Pi= trunc(Nr)
print(f' O número {Nr} tem a parte Inteira {Pi}')