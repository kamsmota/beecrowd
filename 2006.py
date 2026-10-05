# Identificando o chá
tipo = int(input())

# map aplica o split no input, e depois transforma seus resultados em inteiros
competidores = map(int, input().split())

certo = 0

# para cada item da "lista" competidores
for i in competidores:
    if (i == tipo):
        certo += 1
    
print(certo)
