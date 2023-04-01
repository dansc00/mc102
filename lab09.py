# Daniel de Sousa Cipriano RA: 233228

def teste(a,b):
    for x in range(1,n+1):
        if (a * x == b) or (b * x == a):
            return True
        else:
            continue

n = int(input())
cont = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        r = (teste(j,i))
        if (r == True):
            print('*', end="")
            cont += 1
        else:
            print('-', end="")
    print()
print(cont)
