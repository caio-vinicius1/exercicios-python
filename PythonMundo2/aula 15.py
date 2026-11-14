# Aula 15: interropendo laço com break
n = s = 0  # n = começa de 0 e s = começa de 0
while True: # Enquanto for verdadeiro = Loop infinito!
    n = int(input('Digite um número: '))
    if n == 999: # O 999 não vai ser somado, ele é o termo de parada
        break    # break: interrompa o laço
    s += n       # soma dos valores retirando o 999
print(f'A soma vale {s}')