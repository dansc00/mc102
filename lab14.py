# Daniel de Sousa Cipriano RA: 233228

def imp(a): # op p imprime
    for ra in a:
        if ra != a[-1]:
            print(ra, end=' ')
        else:
            print(ra, end='')
            print(' ')
#-----------------------------------------------------------------------------------------------------------
def ordcresc(b): # op c ordenação crescente
    for i in range(len(b)-1,0,-1):
        for j in range(i):
            if b[j] > b[j+1]:
                b[j],b[j+1] = b[j+1],b[j]

#-----------------------------------------------------------------------------------------------------------
def orddecresc(c): # op d ordenação decrescente
    for i in range(len(c)-1,0,-1):
        for j in range(i):
            if c[j] < c[j+1]:
                c[j],c[j+1] = c[j+1],c[j]

#-----------------------------------------------------------------------------------------------------------
def bbin(d,busc): # op b busca binária
    global orde1
    global orde2
    primeiro = 0
    ultimo = len(d)-1
    if orde1 == True:
        while primeiro <= ultimo:
            meio = (primeiro+ultimo)//2
            if d[meio] == busc:
                print(meio, end='')
                print(' ')
                print('{} esta na posicao: {}'.format(busc,meio))
                return None
            elif d[meio] > busc:
                ultimo = meio - 1
                print(meio, end=' ')
            elif d[meio] < busc:
                primeiro = meio + 1
                print(meio, end=' ')

        print()
        print('{} nao esta na lista!'.format(busc))

    elif orde2 == True:
        while primeiro <= ultimo:
            meio = (primeiro+ultimo)//2
            if d[meio] == busc:
                print(meio, end='')
                print(' ')
                print('{} esta na posicao: {}'.format(busc,meio))
                return None
            elif d[meio] < busc:
                ultimo = meio - 1
                print(meio, end=' ')
            elif d[meio] > busc:
                primeiro = meio + 1
                print(meio, end=' ')

        print()
        print('{} nao esta na lista!'.format(busc))


    elif orde1 == False and orde2 == False:
        print('Vetor nao ordenado!')




#-----------------------------------------------------------------------------------------------------------
def ins(e,ins): # op i inserir
    global orde1
    global orde2
    if len(e) != 150 and ins not in e:
        if orde1 == True and orde2 == False:
            e.append(ins)
            for i in range(len(e)-1,0,-1):
                for j in range(i):
                    if e[j] > e[j+1]:
                        e[j],e[j+1] = e[j+1],e[j]

        elif orde2 == True and orde1 == False:
            e.append(ins)
            for i in range(len(e) - 1, 0, -1):
                for j in range(i):
                    if e[j] < e[j + 1]:
                        e[j], e[j + 1] = e[j + 1], e[j]


        elif orde1 == False and orde2 == False:
            e.append(ins)


    elif len(e) != 150 and ins in e:
        print('Aluno ja matriculado na turma!')
    else:
        print('Limite de vagas excedido!')
#----------------------------------------------------------------------------------------------------------
def rem(f,remov): # op r remover
    if len(f) != 0 and remov in f:
        f.remove(remov)

    elif len(f) == 0 and remov not in f:
        print('Nao ha alunos cadastrados na turma!')
    elif len(f) != 0 and remov not in f:
        print('Aluno nao matriculado na turma!')
#----------------------------------------------------------------------------------------------------------
ra = input().split() # lista de ra's
ra = [int(e) for e in ra] # transformas os ra's em inteiros
ops = ''
orde1 = orde2 = False

while True:
    ops = input().split()

    if ops[0] != 's':

        if ops[0] == 'p':
            imp(ra)

        elif ops[0] == 'c':
            ordcresc(ra)
            orde1 = True
            orde2 = False

        elif ops[0] == 'd':
            orddecresc(ra)
            orde2 = True
            orde1 = False

        elif ops[0] == 'b':
            bbin(ra,int(ops[1]))

        elif ops[0] == 'i':
            ins(ra,int(ops[1]))


        elif ops[0] == 'r':
            rem(ra, int(ops[1]))

    else:
        break
