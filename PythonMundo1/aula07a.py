# Envolvendo operadores aritiméticos na nova sintaxe.
# \n: para quebra de linha
# end='': para continuação de linha
#{:3f}: adição de casas decimais a números floats(flutuantes 3.33)
n1=int(input('Digite um valor: '))
n2=int(input('Outro valor: '))
S=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2
print('A soma é:{},\nO produto é:{}\nA divisão é:{:.2f}'.format(S,m,d), end='')
print('\nDivisão inteira é:{}\nE a potência é:{}'.format(di,e))