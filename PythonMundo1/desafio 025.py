#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome= input('Digite seu nome: ').strip()
nome_maiusculo= nome.upper()
nome2= "SILVA" in nome_maiusculo
print(f'Há o nome "SILVA" no seu nome completo:{nome}?\n{nome2}')
 