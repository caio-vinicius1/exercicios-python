#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou
# não formar
# um triângulo.
#exemplo:
# r1-------
# r2-------
# r3-------
r1= float(input('Digite o tamanho da reta 1: '))
r2= float(input('Digite o tamanho da reta 2: '))
r3= float(input('Digite o tamanho da reta 3: '))
#primeiro teste
if r1<r2+r3:
    if r2<r1+r3:
        if r3<r1+r2:
            print('Pode formar triângulo')
        else:
            print('Não pode formar o triângulo')
    else:
        print('Não pode formar o triângulo')
else:
    print('Não pode formar o triângulo')