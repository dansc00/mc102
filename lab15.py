#!/usr/bin/env python3
#*******************************************************************************
# Funcao: atualizaTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato
#   jogo: string contendo as informações de um jogo no formato especificado no lab.
#
# Descrição:
#   Deve inserir as informações do parametro 'jogo' na tabela.
#   OBSERVAÇÃO: nesse momento não é necessário ordenar a tabela, apenas inserir as informações.

def atualizaTabela(tabela, jogo):
    jogo = jogo.split() # transforma jogo em uma lista de strings
    jogo[1], jogo[3] = int(jogo[1]), int(jogo[3]) # transforma os placares em inteiros

    for l in range(len(tabela)): # percorre a seção para cada time na tabela
        if tabela[l][0] == jogo[0]: # testa se a tabela na posição [l][0] é o time que joga em casa
            if jogo[1] > jogo[3]: # caso time da casa vencedor
                tabela[l][1] += 3
                tabela[l][2] += 1
                tabela[l][3] += jogo[1] - jogo[3]
                tabela[l][4] += jogo[1]
            elif jogo[1] < jogo[3]: # caso time da casa perdedor
                tabela[l][3] += (jogo[1] - jogo[3])
                tabela[l][4] += jogo[1]
            elif jogo[1] == jogo[3]: # caso times empataram
                tabela[l][1] += 1
                tabela[l][4] += jogo[1]

        elif tabela[l][0] == jogo[4]: # se a tabela na posição [l][0] é o time visitante
            if jogo[3] > jogo[1]: # caso time visitante vencedor
                tabela[l][1] += 3
                tabela[l][2] += 1
                tabela[l][3] += jogo[3] - jogo[1]
                tabela[l][4] += jogo[3]
            elif jogo[3] < jogo[1]: # caso time visitante perdedor
                tabela[l][3] += (jogo[3] - jogo[1])
                tabela[l][4] += jogo[3]
            elif jogo[3] == jogo[1]: # caso times empataram
                tabela[l][1] += 1
                tabela[l][4] += jogo[3]

# Funcao: comparaTimes
#
# Parametros:
#   time1: informações de um time
#   time2: informações de um time
#
# Descricão:
#   retorna 1, se o time1>time2, retorna -1, se time1<time2, e retorna 0, se time1=time2
#   Observe que time1>time2=true significa que o time1 deve estar em uma posição melhor do que o time2 na tabela.

def comparaTimes(time1, time2):
    if time1[1] > time2[1]:
        return 1
    elif time1[1] < time2[1]:
        return -1
    elif time1[1] == time2[1]:
        return 0


# Funcao: ordenaTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato.
#
# Descricão:
#   Deve ordenar a tabela com campeonato de acordo com as especificaçoes do lab.
#
def ordenaTabela(tabela):

    for i in range(len(tabela)-1,0,-1): # percorre a tabela do penúltimo valor até o primeiro(times)
        for j in range(i): # percorre cada time, necessário para o Bubble Short
            time1 = tabela[j]
            time2 = tabela[j+1]
            if comparaTimes(time1,time2) == 1: # primeira comparação, time1 mais pontos que time2, mantém
                continue
            elif comparaTimes(time1,time2) == -1: # segunda compração, time1 menos pontos que time2, troca posição
                tabela[j], tabela[j+1] = tabela[j+1], tabela[j]
            elif comparaTimes(time1,time2) == 0: # terceira comparação, times empatados
                if time2[2] > time1[2]: # se time 2 mais vitorias que time1, troca
                    tabela[j], tabela[j+1] = tabela[j+1], tabela[j]
                elif time2[2] < time1[2]: # se time2 menos vitorias que time1 mantém
                    continue
                elif time2[2] == time1[2]: # se empatados em vitorias
                    if time2[3] > time1[3]: # se time2 maior saldo de gols que time1
                        tabela[j], tabela[j+1] = tabela[j+1], tabela[j]
                    elif time2[3] < time1[3]: # se time2 menor saldo de gols que time1, mantém
                        continue
                    elif time2[3] == time1[3]: # se empatados em saldo de gols e vitorias
                        if time2[4] > time1[4]: # se time2 mais gols pró, troca
                            tabela[j], tabela[j+1] = tabela[j+1], tabela[j]
                        elif time2[4] < time1[4]:# se time2 menos gols pró, mantém
                            continue
    return tabela

#*******************************************************************************
# Funcao: imprimeTabela
#
# Parametros:
#   tabela: uma matriz com os dados da tabela do campeonato.
#
# Descrição:
#   Deve imprimir a tabela do campeonato de acordo com as especificações do lab.
def imprimeTabela(tabela):

    for i in tabela: # percorre a tabela
        cont = 0 # contador de elementos
        for j in i: # percorre cada elemento da tabela
            cont += 1
            if cont < 5:
                print(j, end=', ') # se n for o último elemento, printa com vírgula e espaço
            else:
                print(j) # se for o último elemento, printa normal e pula linha
