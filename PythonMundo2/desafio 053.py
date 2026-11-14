# Crie um programa que leia uma frase qualquer e diga se ela 
# é um palíndromo, desconsiderando os espaços.
frase_invertida = []
frase = str(input('Digite uma frase: ').upper().replace(' ',''))
for c in range(len(frase)- 1, -1, -1):
    frase_invertida.append(frase[c])
junta = "".join(frase_invertida)
if junta == frase:
    print('É PALÍNDROMO')
else:
    print('NÃO É UM PALÍNDROMO')
