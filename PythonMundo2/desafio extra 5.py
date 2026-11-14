# Nível 3: usando o valor do laço
# Tabuada do 3 (3 x 1 = 3 até 3 x 10 = 30).
n = int(input('Digite um número: '))
for c in range(1,11):
    print(f'{n} x {c} = {n * c}')
#Imprima o quadrado de cada número de 1 a 5:
for c in range(1,6):
    print(f'O quadrado de {c} é {c*c}.')