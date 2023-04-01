# Daniel de Sousa Cipriuano RA: 233228
# Programa que leia um certo tempo de duração de um escudo e calcule se com uma certa quantia de combustível, que está sendo perdido, é possível atingir a dobra espacial antes que a aeronave seja destruida

#Entrada

t = int(input())
c = int(input())
nums = input()
seq = nums.split()

#Saída
soma = int(seq[0])
for y in range (0,t):
    if y == 0:
        if int(seq[y]) >= c:
            print("sim")
        else:
            continue
    else:
        soma += int(seq[y])
        if soma >= c:
            print("sim")
            print("{}".format(y+1))
            break
        else:
            continue
if soma < c:
    print("nao")
    print("{}".format(t+1))
