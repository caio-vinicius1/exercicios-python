#Crie um programa que leia o nome completo de uma pessoa e mostre:
	#O nome com todas as letras maiúsculas.
	#O nome com todas minúsculas.
	#Quantas letras ao todo (sem considerar espaços).
	#Quantas letras tem o primeiro nome.
nome= (input('Digite seu nome completo: '))
maiusculo= nome.upper()
minusculo= nome.lower()
nome_sem_espaco= nome.replace(" ","")
total_letras= len(nome_sem_espaco)
dividir_nome= nome.split()
pegar_o_primeiro_nome= dividir_nome[0]
quantas_letras_primeiro_nome= len(pegar_o_primeiro_nome)
print(f'{maiusculo}, {minusculo}, {total_letras}, {quantas_letras_primeiro_nome}')