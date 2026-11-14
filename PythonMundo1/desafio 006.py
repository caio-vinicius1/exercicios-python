#Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raíz quadrada.
n=int(input('Digite um valor: '))
d=n*2
t=n*3
r=int(n**(1/2))
print('O drobro de {} é {},\nO triplo é:{},\nA raíz quadrada é:{}'.format(n,d,t,r))