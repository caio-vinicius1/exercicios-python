# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Digite seu sexo: ').strip().upper())
while sexo not in ('M', 'F'):
    print('DIGITO INVÁLIDO! DIGITE NOVAMENTE APENAS M OU F.')
    sexo = str(input('Digite seu sexo: ').strip().upper())
print(f'seu sexo é: {sexo}')
