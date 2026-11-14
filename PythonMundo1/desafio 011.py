#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

La= float(input('Qual a largura da parede?:'))
aL= float(input('Qual a altura da parede?:'))
area= La*aL
tinta= area/2
print(f'a largura da parede é {La:.2f} metros \na altura é {aL:.2f} metros \na area corresponde a {area:.2f} metros quadrados \na quantidade de tinta necessaria \npara pintá-la é {tinta:.2f} litros')
