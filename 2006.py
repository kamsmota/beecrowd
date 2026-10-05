# Identificando o chá
tipo = int(input())
competidores = map(int, input().split())

certo = 0
for i in competidores:
    if (i == tipo):
        certo += 1
    
print(certo)
