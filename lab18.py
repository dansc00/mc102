# Daniel de Sousa Cipriano RA: 233228

import sys

def cria_matriz(m, arquivo): # cria a matriz m a partir da referencia r que possui o arquivo e o comprimento de m(cm)
    for x in arquivo:
        m.append(x.split()) # adiciona os elementos de cada linha do arquivo na matriz

def transforma_inteiros(m): # transforma os str da matriz em inteiros
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = int(m[i][j]) #transforma os elementos em inteiros

def convolucao(i, m, d): # recebe i: matriz imagem, m: matriz nucleo, d = divisor. Realiza a convolução
    i_ = [i[x].copy() for x in range(len(i))] # cria matriz i_ cópia da matriz imagem
    for linha in range(1,len(i)-1): # percorre as linhas da matriz imagem
        for coluna in range(1, len(i[linha])-1): # pecorre as colunas da matriz imagem
            # soma da convolução
            soma = ((i[linha-1][coluna-1] * m[0][0]) + (i[linha-1][coluna] * m[0][1]) + (i[linha-1][coluna+1]*m[0][2]) + (i[linha][coluna-1]*m[1][0]) + (i[linha][coluna]*m[1][1]) + (i[linha][coluna+1]*m[1][2]) + (i[linha+1][coluna-1]*m[2][0]) + (i[linha+1][coluna]*m[2][1]) + (i[linha+1][coluna+1]*m[2][2]))/d
            if soma < 0:  # limitantes
                soma = 0
            elif soma > 255:
                soma = 255
            i_[linha][coluna] = int(soma) # adiciona novo elemento à matriz cópia da imagem
    return i_ # retorna a matriz resultado da convolucao

#-----------------------------------------------------------------------------------------------------------------------------------------
arq = open(sys.argv[1], 'r') # abre o arquivo imagem no modo apenas leitura
matriz_img = [] # matriz imagem
cria_matriz(matriz_img, arq)
#-----------------------------------------------------------------------------------------------------------------------------------------
arq2 = open(sys.argv[2], 'r') # abre o arquivo contendo a matriz nucleo e o valor de d
d = arq2.readline() # adiciona d
matriz_nucleo = [] # matriz nucleo
cria_matriz(matriz_nucleo, arq2)
#------------------------------------------------------------------------------------------------------------------------------------------
transforma_inteiros(matriz_img[3:]) # chama a func para transformar os valores em inteiros
transforma_inteiros(matriz_nucleo)
#------------------------------------------------------------------------------------------------------------------------------------------
matriz_resultado = convolucao(matriz_img[3:], matriz_nucleo, int(d)) # resultado da convolução
resultado = open('resultadolab18.pgm','w+') # escreve na imagem resultante
resultado.write('P2\n')
resultado.write(matriz_img[1][0]+' ')
resultado.write(matriz_img[1][1])
resultado.write('\n255\n')

print(matriz_img[0][0])  # print das primeiras linhas
print(matriz_img[1][0], end=' ')
print(matriz_img[1][1])
print(matriz_img[2][0])
for i in matriz_resultado: # printa a matriz e adiciona as linhas a imagem resultante
    for j in range(len(i)):
        if j != len(i)-1:
            print(i[j], end=' ')
        else:
            print(i[j], end='  ')
        resultado.write(str(i[j])+' ')
    resultado.write('\n')
    print()

arq.close() # fecha arquivos
arq2.close()
resultado.close()
