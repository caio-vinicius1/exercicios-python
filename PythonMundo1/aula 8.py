#Aula 8 -- Utilizando Módulos
import math
num= int(input('Digite um número: '))
raiz= math.sqrt(num)
print(f'A raiz de {num} é igual a {raiz:.2f}')
#Outro tipo de importação de módulo
from math import  sqrt, floor
num= int(input('Digite um número: '))
raiz= sqrt(num)
print(f'A raiz de {num} é igual a {floor(raiz)}')
