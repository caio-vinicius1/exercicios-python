# Faça um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com sua idade: 
# - Se ele ainda vai se alistar ao serviço militar. 
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
sexo = str(input('Qual seu sexo: ').upper())
ano = int(input('Qual o seu ano de nascimento? '))
idade = date.today().year - ano
if sexo == ('feminino'.upper()):
    print('O seu alistamento não é obrigatória')
elif idade < 18:
    print(f'Você tem {idade} anos, ainda irá se alistar ao serviço militar!')
    print(f'Ainda falta {18-idade} anos para o seu alistamento.')
elif idade == 18:
    print(f'Você tem {idade} anos, é hora de se alistar!')
elif idade > 18:
    print(f'Você tem {idade} anos, já passou o tempo do seu alistamento em {idade-18} anos!')
print('Para mais informações, procure uma junta de serviço militar!')
 