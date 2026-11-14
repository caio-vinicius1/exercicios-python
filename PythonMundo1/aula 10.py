nome=str(input('Qual o seu nome?: '))
nome=nome.upper()
if nome== 'CAIO':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print(f'Bom dia, {nome}!')
#Outro exemplo>>>>>>>>>>>>>>>>
n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
m=(n1+n2)/2
print(f'A sua média foi {m:.1f}')
if m>=6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')