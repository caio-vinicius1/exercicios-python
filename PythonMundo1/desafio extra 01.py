#Leia o ano de nasimento e diga a idade, e se a pessoa ainda não vota (menos de 16 anos ), se o voto é obrigatório (18 a 69) ou opcional.
ano_de_nascimento = int(input('Digite o ano de nascimento: '))
idade= 2026 - ano_de_nascimento
print(f'A sua idade é: {idade}')
if idade>=16:
    print('Você pode votar!')
    if 18 <= idade <= 69:
        print('Seu voto é obrigatório!')
    else:
        print('Seu voto não é obrigatório!')
else:
    print('Você não pode votar!')