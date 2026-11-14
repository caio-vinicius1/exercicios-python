#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#exemplo: Ana Maria de Souza
# primeiro=Ana
# último=Souza
nome=input('Digite seu nome completo: ').strip()
nome=nome.split()
primeiro_nome=nome[0]
ultimo_nome=nome[-1]
print(f'Primeiro nome= {primeiro_nome}\n'
      f'Último nome= {ultimo_nome}')