#Exemplo do carro, com vários caminhos:
# if carro.esquerda():
# bloco 1
# elif carro.direita():
# bloco 2
# elif carro.ré():
# bloco 3
# else:
# bloco 4
# CÓDIGO:
nome= str(input('Qual o seu nome? '))
if nome == 'Caio':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome== 'Maria' or nome== 'Paulo':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Fracisca Paula Jéssica Vitória':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem peculiar')
print(f'Tenha um bom dia, {nome}!')