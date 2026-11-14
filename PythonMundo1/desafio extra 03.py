#Leia três lados e diga se formam um triângulo(cada lado menor que a soma dos outros dois).
#Se formarem, diga se é equilátero, isósceles o escaleno.
lado1= float(input('Digite um lado do triângulo: '))
lado2= float(input('Digite um outro lado do triângulo: '))
lado3= float(input('Digite um outro lado do triângulo: '))
if lado1 < lado2 + lado3:
    if lado2 < lado1 + lado3:
        if lado3 < lado1 + lado2:
            print('Pode formar um triângulo!')
        else:
            print('Não forma um triângulo!')
    else:
        print('Não forma um triângulo!')
else:
    print('Não forma um triângulo!')