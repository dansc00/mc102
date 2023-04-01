# Daniel de Sousa Cipriano RA: 233228

def transforma_inteiros(m): # transforma os elementos de m em inteiros
    m_int = []
    for i in range(len(m)):
        m_int.append([])
        for j in m[i]:
            m_int[i].append(int(j))
    return m_int

def cadeia(m, k, sub):
    for i in range(len(m[k])): # percorre o comprimento da linha que indica o funcionario k
        if m[k][i] == 1: # se == 1, é um subordinado
            sub.append(i) # adiciona o subordinado a lista subordinados
            cadeia(m, i, sub) # começa a recursão identificando o subordinado do subordinado...
    return sub.sort()

nk = input().split() # lista com n e k
n = int(nk[0]) # n inteiro
k = int(nk[1]) # k inteiro
matriz_funcionarios = [] # matriz quadrada com os funcionarios
matriz_subordinados = [] # matriz com os subordinados, começa com o proprio k
for cont in range(n): # cria a matriz funcionarios
    matriz_funcionarios.append(input().split())

matriz_funcionarios = transforma_inteiros(matriz_funcionarios)
cadeia(matriz_funcionarios, k, matriz_subordinados)
matriz_subordinados.append(k)

if len(matriz_subordinados) == 1:
    print(matriz_subordinados[0])
else:
    print(matriz_subordinados[-1], end=' ')
    
for res in matriz_subordinados: # imprime os subordinados
    if res != matriz_subordinados[-1]:
        if res != matriz_subordinados[-2]:
            print(res, end=' ')
        else:
            print(res)
