# desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritimética(PA). 
# No final, mostre os 10 primeiros termos dessa progressão.
a1 = int(input('Digite o primeiro termo: ')) # de onde a progressão começa.
r = int(input('Digite a razão: ')) # quanto você soma a cada passo.
for c in range(10):
    termo = a1 + (c * r) 
    print(termo)
