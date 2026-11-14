# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n
#  primeiros elementos de uma Sequência de FIBONACCI.
# EX: 0 - 1 - 1 - 2 - 3 - 5 - 8
n = int(input('Digite um número inteiro: '))
t1 = 0   # A sequência de Fibonacci já começa o com 0 e 1.
t2 = 1   # Por isso duas variáveis chamadas t1 e t2. 
c = 2    # A variável do contador das voltas do laço (while).
print(f'{t1} - {t2}', end='')  # Print para colocar já os dois termos no ínicio (t1,t2/0,1).
while c < n:                   # Enquanto c for menor que n. REPITA!
    t3 = t1 + t2               # Todo o bloco de dentro do while vai ser repetido, até a condição for falsa.
    print(f' - {t3}', end='')   # print do (t3): a soma de t1 + t2 (0 + 1)
    t1 = t2                    # Substituiçao dos velhos valores por novos.
    t2 = t3
    c = c + 1                  # O contador das voltas do laço (while).
print(' - FIM')                 # print Final, depois que while se torna falso.
