#!/usr/bin/env python3

import math

# Laboratorio 17 - Banco de Dados Geografico
# Nome: Daniel de Sousa Cipriano
# RA: 233228

class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Cidade:
    def __init__(self, coordenadas, inicioCEP, fimCEP, numHabitantes):
        self.coordenadas = coordenadas
        self.inicioCEP = inicioCEP
        self.fimCEP = fimCEP
        self.numHabitantes = numHabitantes

#
# Funcao: distancia
#
# Parametros:
#   a, b: pontos
#
# Retorno:
#   A distancia euclidiana entre a e b.
#
def distancia(c1, c2):
    return int(100 * math.sqrt((c1.x - c2.x)**2 + (c1.y - c2.y)**2)) / 100.0

# Funcao: consulta_cidade_por_cep
#
# Parametros:
#   cidades: lista de cidades (base de dados)
#       cep: CEP desejado
#
# Retorno:
#   O indice da cidade que contem o CEP desejado ou None caso não haja tal cidade.
#
def consulta_cidade_por_cep(cidades, cep):
    for x in range(len(cidades)): # percorre o comprimento da lista de cidades
        if cep in range(cidades[x].inicioCEP,cidades[x].fimCEP):# para cada cidade, testa se a faixa de ceps se encaixa dentro do cep buscado
            return x # retorna o indice da cidade caso verdadeiro
    return None

# Funcao: consulta_cidades_por_raio
#
# Parametros:
#            cidades: lista de cidades (base de dados)
#   cidadeReferencia: indice da cidade referencia (centro da circunferencia)
#               raio: raio da busca
#
# Retorno:
#   Lista dos indices das cidades que estao contidas no raio de busca (incluindo
#   a cidade referencia) *ordenados pelas respectivas distancias da cidade referencia*.
#
def consulta_cidades_por_raio(cidades, cidadeReferencia, raio):
    indices = [cidadeReferencia] # lista de indices
    ldist = [distancia(cidades[cidadeReferencia].coordenadas, cidades[cidadeReferencia].coordenadas)] # lista de distancias
    for x in range(len(cidades)): # percorre o comprimento da lista cidades
        if x != cidadeReferencia: # se o indice for diferente do indice referencia
            dist = distancia(cidades[cidadeReferencia].coordenadas, cidades[x].coordenadas) # chama a função e salva o valor da distancia entre 2 pontos na variavel
            if dist <= raio: # se a distancia esta dentro do raio pedido
                ldist.append(dist) # lista de distancias recebe a distancia medida
                indices.append(x) # adiciona o indice da cidade na lista de indices

    for i in range (len(ldist)-1, 0, -1): # bubble sort
        for j in range(i):
            if ldist[j+1] < ldist[j]:
                ldist[j], ldist[j+1] = ldist[j+1], ldist[j] #ordena a lista de distancias
                indices[j], indices[j+1] = indices[j+1], indices[j] #ordena a lista de indices
    return indices

# Funcao: populacao_total
#
# Parametros:
#            cidades: lista de cidades (base de dados)
#   cidadeReferencia: indice da cidade referencia (centro da circunferencia)
#               raio: raio da busca
#
# Retorno:
#   O numero de habitantes das cidades que estao contidas no raio de busca
#
def populacao_total(cidades, cidadeReferencia, raio):
    pop = cidades[cidadeReferencia].numHabitantes # população começa com o n de habitantes da cidade referencia
    for x in range (len(cidades)):
        if x != cidadeReferencia:
            dist = distancia(cidades[cidadeReferencia].coordenadas, cidades[x].coordenadas)
            if dist <= raio:
                pop += cidades[x].numHabitantes # adiciona o n de habitantes das cidades dentro do raio a população total
    return pop

# Funcao: mediana_da_populacao
#
# Parametros:
#            cidades: lista de cidades (base de dados)
#   cidadeReferencia: indice da cidade referencia (centro da circunferencia)
#               raio: raio da busca
#
# Retorno:
#   Mediana do numero de habitantes das cidades que estao contidas no raio de busca
#
def mediana_da_populacao(cidades, cidadeReferencia, raio):
    med = [cidades[cidadeReferencia].numHabitantes] # lista com o n de habitantes começa com o n de habitantes da cid referencia
    for x in range(len(cidades)):
        if x != cidadeReferencia:
            dist = distancia(cidades[cidadeReferencia].coordenadas, cidades[x].coordenadas)
            if dist <= raio:
                med.append(cidades[x].numHabitantes) # adiciona as populações das cidades
    med.sort() # ordena a lista
    if len(med) % 2 != 0:
        meio = len(med)//2 # calcula o indice do meio caso o comprimento da lista seja um n impar
        return med[meio]
    else:
        meio = len(med)//2
        meio2 = (len(med)//2)-1
        mediana = (med[meio] + med[meio2])/2
        return mediana
