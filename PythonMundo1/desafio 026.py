#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A".
#Em que posição ela aparece a primeira vez.
#Em que posição ela aparece a última vez.
frase=input('Digite uma frase qualquer: ')
frase=frase.strip()
frase=frase.upper()
quantas_letra_a= frase.count('A')
primeira_posicao=frase.find('A')
ultima_posicao=frase.rfind('A')
print(f'Quantas vezes aparece a letra "A"?: {quantas_letra_a}\n'
      f'Em que posição ela aparece a primeira vez?: {primeira_posicao+1}\n'
      f'Em que posição ela aparece a última vez?: {ultima_posicao+1}')