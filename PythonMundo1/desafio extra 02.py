from random import randint
#Sortei um número de 1 a 10 com random. O usuário tenta adivinhar, e o programa diz se acertou ou errou.
n= int(input('Digite um número que estou pensando: '))
sorteado= randint(1,10)
if n == sorteado:
    print(f'Você acertou! O escolhido por mim é o {sorteado}')
else:
    print(f'Você errou! O escolhido por mim é o {sorteado}')
