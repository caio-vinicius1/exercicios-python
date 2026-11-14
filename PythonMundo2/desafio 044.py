# Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
# À vista dinheiro / cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros
produto = float(input('Digite o valor do produto (use vírgula nos centavos): ').replace('.','').replace(',','.'))
print('FORMAS DE PAGAMENTO:\n1- À vista dinheiro / cheque: 10% de desconto\n2- À vista no cartão: 5% de desconto\n' \
'3- Em até 2x no cartão: preço normal\n4- 3x ou mais no cartão: 20% de juros'.upper())
forma_de_pagamento = int(input('Qual a forma de pagamento? '))
if forma_de_pagamento == 1:
    # À vista dinheiro / cheque: 10% de desconto
     dinheiro_cheque = produto - (produto * 0.10)
     print(f'O produto ficou no valor de R${produto:.2f}, com a forma de pagamento 1, o valor do produto é: R${dinheiro_cheque:.2f}')
elif forma_de_pagamento == 2:
     # À vista no cartão: 5% de desconto
     a_vista_cartao = produto - (produto * 0.05)
     print(f'O produto ficou no valor de R${produto:.2f}, com a forma de pagamento 2, o valor do produto é: R${a_vista_cartao:.2f}')
elif forma_de_pagamento == 3:
     # Em até 2x no cartão: preço normal
     duas_vezes_cartao = produto
     print(f'O produto ficou no valor de R${produto:.2f}, com a forma de pagamento 3, o valor com parcelas ficou em: R${duas_vezes_cartao:.2f}')
elif forma_de_pagamento == 4:
     # 3x ou mais no cartão: 20% de juros
     tres_vezes_mais_cartao = produto + (produto * 0.20)
     print(f'O produto ficou no valor de R${produto:.2f}, com a forma de pagamento 4, o valor do produto é: R${tres_vezes_mais_cartao:.2f}')
else:
     print('Opção inválida')
