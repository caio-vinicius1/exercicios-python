# VERSÃO CORRIGIDA
# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
valor_um = int(input('Digite um valor: '))
valor_dois = int(input('Digite outro valor: '))
escolha = 0

while escolha != 5:
    print('MENU: Digite o valor da opção!')
    print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa')
    escolha = int(input('Qual a opção? '))
    if escolha == 1:
       print('OPÇÃO 1: SOMAR')
       print(f'A soma dos valores {valor_um} e {valor_dois} é {valor_um + valor_dois}.')
    elif escolha == 2:
       print('OPÇÃO 2: MULTIPLICAR')
       print(f'A multiplicação dos valores {valor_um} e {valor_dois} é {valor_um * valor_dois}.')
    elif escolha == 3:
        print('OPÇÃO 3: MAIOR')
        if valor_um > valor_dois:
            print(f'O maior valor entre os dois digitados é {valor_um}.')
        elif valor_um < valor_dois:
            print(f'O maior valor entre os dois digitados é {valor_dois}.')
        else:
            print('Os dois valores são iguais')
    elif escolha == 4:
       print('OPÇÃO 4: NOVOS NÚMEROS')
       valor_um = int(input('Digite um valor: '))
       valor_dois = int(input('Digite outro valor: '))
    elif escolha == 5:
       print('Programa encerrado com sucesso!')
    else:
       print('Opção inválida! Tente novamente.')
print('Finalizando...')
sleep(2)
print('Fim do programa!')

'''
VERSÃO ANTIGA (com erros)
Problemas:
- o menu só voltava se escolhesse a opção 4
- operações duplicadas dentro e fora do while
- comparação do "maior" feita com soma dos valores
- opção 4 criava variáveis extras em vez de substituir os valores

# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

valor_um = int(input('Digite um valor: '))
valor_dois = int(input('Digite outro valor: '))
print('MENU: Digite o valor da opção!')
print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa')
escolha = int(input('Qual a opção? '))
while escolha == 4:
  valor_novo = int(input('Digite outro valor: '))
  valor_novo_1 = int(input('Digite mais outro:'))
  print('[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa')
  escolha = int(input('Qual a sua opção? '))
  if escolha == 1:
      print('OPÇãO 1: SOMAR')
      print(f'A soma dos valores {valor_um}, {valor_dois}, {valor_novo} e {valor_novo_1} é {valor_um + valor_dois + valor_novo + valor_novo_1}')
  elif escolha == 2:
      print('OPÇÃO 2: MULTIPLICAR')
      print(f'A multiplicação dos valores {valor_um}, {valor_dois}, {valor_novo} e {valor_novo_1} é {valor_um * valor_dois * valor_novo * valor_novo_1}')
  elif escolha == 3:
      print('OPÇÃO 3: MAIOR')
      if valor_um > valor_dois and valor_novo and valor_novo_1:
          print(f'O maior valor entre os digitados é {valor_um}')
      elif valor_dois > valor_um + valor_novo + valor_novo_1:
          print(f'O maior valor entre os digitados é {valor_dois}')
      elif valor_novo > valor_um + valor_dois + valor_novo_1:
          print(f'O maior valor entre oa digitados é {valor_novo}')
      else:
          print(f'O maior valor entre os digitados é {valor_novo_1}')
if escolha == 1:
    print('OPÇÃO 1: SOMAR')
    print(f'A soma dos valores {valor_um} e {valor_dois} é {valor_um + valor_dois}.')
elif escolha == 2:
    print('OPÇÃO 2: MULTIPLICAR')
    print(f'A multiplicação dos valores {valor_um} e {valor_dois} é {valor_um * valor_dois}.')
elif escolha == 3:
    print('OPÇÃO 3: MAIOR')
    if valor_um > valor_dois:
        print(f'O maior valor entre os dois digitados é {valor_um}.')
    elif valor_um < valor_dois:
        print(f'O maior valor entre os dois digitados é {valor_dois}.')
elif escolha == 5:
    print('Programa encerrado com sucesso!')'''
