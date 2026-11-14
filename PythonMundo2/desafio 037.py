# Escreva um programa que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de conversão: 
# -1 para binário 
# -2 para octal 
# -3 para hexadecimal
n = int(input('Digite um número: '))
print('1- binário, 2-octal, 3- hexadecimal')
base_de_conversao = str(input('Qual será a base de conversão? '))
if base_de_conversao == '1':
    print(f'{n} convertido para binário é {bin(n)[2:]}')
elif base_de_conversao == '2':
    print(f'{n} convertido para octal é {oct(n)[2:]}')
elif base_de_conversao == '3':
    print(f'{n} convertido para hexadecimal é {hex(n)[2:]}')
else:
    print('Opção inválida!')
# Convertido para todas as bases, sem condições aninhadas
n= int(input('Digite um número: '))
print(f'{n} convertido para base de conversão')
print(f'{n} convertido para binário é {bin(n)[2:]}')
print(f'{n} convertido para octal é {oct(n)[2:]}')
print(f'{n} convertido para hexadecimal é {hex(n)[2:]}')
