#!/usr/bin/env python3

# Funcao: pertence
#
# Parametros:
#   conj: vetor contendo o conjunto de entrada
#    num: elemento a ser verificado pertinencia
#
# Retorno:
#   True se num pertence a conj e False caso contrario
#
def pertence(conj, num):
    if num in conj:
        return True
    else:
        return False

# Funcao: contido
#
# Parametros:
#   conj1: vetor contendo um conjunto de entrada
#   conj2: vetor contendo um conjunto de entrada
#
# Retorno:
#   True se conj1 esta contido em conj2 e False caso contrario
#
def contido(conj1, conj2):
    cont = 0
    for e in conj1: # percorre os elementos do conj1
        if e in conj2: # verifica se o elemento e está contido em conj2
            cont += 1 # caso positivo, contador recebe + 1
    if cont == len(conj1): # se o contador equivale ao tamanho do conj1, todos elementos estão contidos
        return True
    else:
        return False

# Funcoes: adicao e subtracao
#
# Parametros:
#   conj: vetor contendo o conjunto que tera incluso ou removido o elemento
#    num: elemento a ser adicionado ou removido
#
def adicao(conj, num):
    if num not in conj:
        conj.append(num)
    return None

def subtracao(conj, num):
    if num in conj:
        conj.remove(num)
    return None

# Funcoes: uniao, intersecao e diferenca
#
# Parametros:
#     conj1: vetor contendo o conjunto de entrada do primeiro operando
#     conj2: vetor contendo o conjunto de entrada do segundo operando
#
# Retorno:
#   Vetor contendo o conjunto de saida/resultado da operacao
#
def uniao(conj1, conj2):
    uconj = conj1.copy()
    for e in conj2:
        if e not in uconj:
            uconj.append(e)
    return uconj

def intersecao(conj1, conj2):
    iconj = []
    for e in conj1:
        if e in conj2:
            iconj.append(e)
    for i in conj2:
        if i in conj1 and i not in iconj:
            iconj.append(i)
    return iconj

def diferenca(conj1, conj2):
    dconj = []
    for e in conj1:
        if e not in conj2:
            dconj.append(e)
    return dconj

def uniao_disjunta(conj1, conj2):
    u_dconj = []
    for e in conj1:
        if e not in conj2:
            u_dconj.append(e)
    for i in conj2:
        if i not in conj1:
            u_dconj.append(i)
    return u_dconj
