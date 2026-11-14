#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario= float(input('Qual o seu salario?:'))
c= salario*0.15
print(f'Parabens você recebeu uma promocao de 15% \n Seu novo salario é:{salario+c:.2f}')