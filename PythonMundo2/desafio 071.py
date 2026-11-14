# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No ínicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas células de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10, R$ 1.
soma = 0
print('BANCO PYTHON')
while True:
    print('Cédulas disponíveis: R$ 50, R$ 20, R$ 10, R$ 1')
    saque = int(input('Qual será o valor a ser sacado? '))
    if saque <= 0:
        while saque <= 0:
            saque = int(input('Valor inválido! Digite novamente: [somente números]: '))
    soma = soma + saque
    quant1 = soma // 50
    saque = soma % 50
    quant2 = saque // 20
    saque = saque % 20
    quant3 = saque // 10
    saque = saque % 10
    quant4 = saque
    outro_saque = str(input('Deseja fazer outro saque? [S/N]: ').upper())
    while outro_saque not in 'SN':
        outro_saque = str(input('Deseja fazer outro saque? [S/N]: ').upper())
    if outro_saque == 'N':
        break
print(soma)
print(f'Serão {quant1} cédulas de R$ 50, {quant2} de R$ 20, {quant3} de R$ 10, {quant4} de R$ 1')
