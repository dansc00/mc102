# Daniel de Sousa Cipriano RA: 233228

def soma(a):
    global mult
    for x in range(len(a)):
        for y in range(x+1, len(a)):
            if a[x] == a[y]:
                mult[x] += mult[y]
                del mult[y]
    return mult

n = int(input())
pca = pcf = i = mult = tot = []
cont = 0
while (cont != n):
    cont += 1
    lista = (input())
    ints = [int(i) for i in lista.split()]
    tot += ints
i = tot[0::3]
pca = tot[1::3]
pcf = tot[2::3]
for z in range(0,n):
    mult[z] = pcf[z]/pca[z]
mult = mult[0:n]
print(i)
print(pca)
print(pcf)
print(mult)

print(soma(i))
