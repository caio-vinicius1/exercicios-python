# A confederação Nacional de Natação precisa de um programa que leia 
# o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#  Até 9 anos: Mirim
#  Até 14 anos: Infantil
#  Até 19 anos: Junior
#  Até 20 anos: Sênior
#  Acima: Master
from datetime import date
print('Categoria por idade\nAté 9 anos: Mirim\nAté 14 anos: Infantil\nAté 19 anos: Junior\nAté 20 anos: Sênior\nAcima: Master')
ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print(f'Você tem {idade} anos, sua categoria é Mirim')
elif idade <= 14:
    print(f'Você tem {idade} anos, sua categoria é Infantil')
elif idade <= 19:
    print(f'Você tem {idade} anos, sua categoria é Junior')
elif idade <= 20:
    print(f'Você tem {idade} anos, sua categoria é Sênior')
else:
    print(f'Você tem {idade} anos, sua categoria é Master')