#Faça um programa que leia um ano qualquer e mostre se ele é Bissexto.
#Guarde uma "cola" com o que já aprendeu:
# % dá o resto da divisão
#resto 0 = divisível
#if dentro de if = perguntas em sequência
#cada else fica na mesma coluna do if dele
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
ano=int(input('Digite um ano: '))
por_4=ano%4
if por_4==0:
    por_100 = ano % 100
    if por_100 == 0:
        por_400 = ano % 400
        if por_400==0:
            print('É Bissexto')
        else:
            print('Não é Bissexto')
    else:
        print('é Bissexto')
else:
    print('Não é Bissexto')
