# Daniel de Sousa Cipriano RA: 233228

mn = input()
mn = [int(e) for e in mn.split()] # LIsta com m e n ( linhas e colunas). mn[0] = linhas e mn[1] = colunas
i = int(input()) # n de dias
matriz = ['' for x in range(mn[0]+2)] # Adiciona as linhas vazias da matriz

for i in range(mn[0]+2): # Roda nas linhas
    matriz[i] = [0 for y in range(mn[1]+2)] # Adiciona zeros em todas linhas
    if i != 0 and i != len(matriz)-1: # Entra nas linhas diferentes da primeira e última
        linha = input()
        matriz[i] = [int(l) for l in linha.split()] # Adiciona elementos para cada coluna nas linhas
        matriz[i].append('')
print(matriz)
