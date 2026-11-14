# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantas anos...
# ele vai pagar.
# Calcule o valor da prestação mensal. Sabendo que ela não pode exceder 30% do salário ou
# então o empréstimo será negado.
print('Empréstimo bancário')
valor_casa = float(input('Qual o valor da casa? ').replace('.','').replace(',','.'))
salario_comprador = float(input('Qual o seu salário? ').replace('.','').replace(',','.'))
pagamento_em_anos = int(input('Em quantos anos você quer pagar? '))
converter_mensal = pagamento_em_anos * 12
calculo_prestacao = valor_casa / converter_mensal
calcular_limite = salario_comprador * 0.30
if calculo_prestacao <= calcular_limite:
    print(f'Valor da prestação: R${calculo_prestacao:.2f}')
    print('Empréstimo aprovado!')
elif calculo_prestacao > calcular_limite:
    print(f'Valor da prestação: R${calculo_prestacao:.2f}')
    print('Empréstimo negado!')


