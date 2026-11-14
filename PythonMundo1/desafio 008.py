#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
#1 metro= 100 centímetros
#1 metro= 1000 milímetros
me=float(input('Digite um valor em metros:'))
cm=me*100
mm=me*1000
print('O valor de {} em cm equivale a:{}\nO valor de {} em mm equivale a:{}'.format(me,cm,me,mm))