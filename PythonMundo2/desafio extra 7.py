# imprima só os números pares de 1 a 20:
for n in range(2, 21, 2):
    print(n)
#  imprima só os múltiplos de 3 de 1 a 30:
detres = []
for i in range(1,31):
    if i % 3 == 0:
       detres.append(i)
print(detres)
# de 1 a 10, imprima "par" ou "ímpar" ao lado de cada número:
par = []
impar = []
for n in range(1, 11):
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(f'Os números pares são: {par}')
print(f'Os números ímpares são: {impar}')
# do jeito que o enunciado pede:
for n in range(1, 11):
    if n % 2 == 0:
        print(n, 'par')
    else:
        print(n, 'ímpar')