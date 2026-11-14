# melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
# palpites foram necessários para vencer.
from random import randint
sorteio = randint(0, 10)
print('Sou o computador e pensei em um número entre 0 e 10. ')
print('Qual o número que eu pensei?')
computador = int(input('Qual número inteiro o computador escolheu:  '))
palpites = 1
while computador != sorteio:
    print('Você não acertou, tente novamente:')
    computador = int(input('Qual número inteiro o computador escolheu: '))
    palpites = palpites + 1
print(f'Você venceu! O número que o computador escolheu é o {sorteio}, você deu {palpites} palpites para vencer.')
