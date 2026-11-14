# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA
# mostrando os 10 primeiros termos da progressão, usando a estrutura
# while.
primeiro_termo = int(input('Digite o primeiro termo da progressão: ')) 
r = int(input('Digite a razão da progressão: '))
c = 0
while c < 10: # O laço lê linha por linha, uma de cada vez
    termo = primeiro_termo + (c * r) # o contador a cada volta ele registra a volta. # na 1° volta o contador está zerado(0)
    print(termo)
    c += 1 # Só depois o contador sobe o número da volta ou adiciona +1.

# o Python executa as linhas de cima para baixo, e quando chega no fim do bloco do while,
#  volta e testa a condição de novo. Se ainda for verdadeira, repete tudo.