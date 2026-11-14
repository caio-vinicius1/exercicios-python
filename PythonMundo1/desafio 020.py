#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
A1= input('Digite o nome do 1° aluno: ')
A2= input('Digite o nome do 2° aluno: ')
A3= input('Digite o nome do 3° aluno: ')
A4= input('Digite o nome do 4° aluno: ')
alunos= [A1, A2, A3, A4]
shuffle(alunos)
print(f'A ordem de apresentação será: {alunos}')
