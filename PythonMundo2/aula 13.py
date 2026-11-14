for c in range(0,3):
    print('157')
print('tu é?')
#
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i,f+1,p):
    print(c)
print('FIM')
#
s = 0
for c in range(0, 5):
    n = int(input('Digite um número: '))
    s += n
print(f'O somatório de todos os valores foi {s}')