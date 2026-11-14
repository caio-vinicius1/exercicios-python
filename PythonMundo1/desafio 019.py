#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
A1= input('Escreva o nome do 1° aluno: ')
A2= input('Escreva o nome do 2° aluno: ')
A3= input('Escreva o nome do 3° aluno: ')
A4= input('Escreva o nome do 4° aluno: ')
alunos= [A1, A2, A3, A4]
so= choice(alunos)
print(f'Aluno escolhido:{so}')
