#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import  pow, sqrt
co= float(input('Digite o comprimento do cateto oposto: '))
ca= float(input('Digite o comprimento do cateto adjacente: '))
co_1= pow(co, 2)
ca_2= pow(ca, 2)
s= co_1 + ca_2
raiz= sqrt(s)
print(f'O comprimento da hipotenusa é {raiz:.2f}')