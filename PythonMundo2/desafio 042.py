# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso 
# de mostrar que tipo de triângulo será formado:
# Equilátero: todod os lados iguais
# isósceles: dois lados iguais.
# Escaleno: todos os lados diferentes.
r1 = float(input('Digite o tamanho da primeira reta: '))
r2 = float(input('Digite o tamanho da segunda reta: '))
r3 = float(input('Digite o tamanho da terceira reta: '))
# Primeiro teste
if r1 < r2+r3:
    if r2 < r1+r3:
        if r3 < r1+r2:
         print('Pode formar triângulo!')
         if r1 == r2 == r3:
             print('Equilátero')
         elif r1 == r2 or r2 == r3 or r3 == r1:
             print('Isósceles')
         else:
             print('Escaleno')
        else:
            print('não pode formar triângulo')
    else:
        print('não pode formar triângulo')
else:
    print('não pode formar triângulo!')


