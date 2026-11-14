#Escreva um programa que pergunte o sálario de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.
salario=float(input('Digite o seu salário: '))
if salario>1250:
    aumento= (salario*0.1)+salario
    print(f'Seu novo salário com 10% de aumento é: R${aumento:.2f}')
else:
    aumento= (salario*0.15)+salario
    print(f'O seu novo salário com 15% de aumento é:{aumento:.2f}')


