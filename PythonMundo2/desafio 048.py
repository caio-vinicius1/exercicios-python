# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos 
# de três e que se encontram no intervalo de 1 até 500.
s = 0 # recebe cada múltiplo de 3 que é == 0, sempre começa em 0
cont = 0
for c in range(1, 501, 2): # inicio, fim e passo.
    if c % 3 == 0: # se c dividido por 3 for resto 0.
        cont = cont + 1
        s = s + c    # acumulador: soma do valor que veio do IF
        print(c)  # Mostra os números ímpares divisíveis por 3
print(f'soma total dos {cont} números ímpares divisíveis por 3 é {s}')

