# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
# quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou
# no final do jogo.
from random import randint
print('JOGO DO PAR OU ÍMPAR')
vitoria = 0
while True:
   print('=' * 30)
   print('Escolha:\n[1] ÍMPAR\n[2] PAR')
   escolha = int(input('ÍMPAR ou  PAR? [1/2]: '))
   n = int(input('Seu número: '))
   computador = randint(1,10)
   resto = (n + computador) % 2
   print(f'computador: {computador}')
   if resto == 0:
     print('PAR')
     if escolha == 2:
       print('Você venceu!')
       vitoria = vitoria + 1
     else:
       print('Você perdeu!')
       break
   elif resto == 1:
     print('ÍMPAR')
     if escolha == 1:
      print('Você venceu!')
      vitoria = vitoria + 1
     else:
      print('Você perdeu!')
      break
print(f'{vitoria} vitória(s) consecutiva(s)')
