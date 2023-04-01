# Daniel de Sousa Cipriano RA: 233228
# Programa que leia o peso de 4 conteineres e calcule se é possível dividir esse peso de maneira igual para a parte dianteira e traseira de uma aeronave.

c1 = int(input())
c2 = int(input())
c3 = int(input())
c4 = int(input())

if (c1 == c2+c3+c4) or (c1 + c2 == c3 + c4) or (c1+c3 == c4 + c2) or (c1 + c4 == c2 + c3) or (c2 == c1+c3+c4) or (c3 == c2+c3+c4) or (c4 == c1+c2+c3):
    print("sim")
else:
    print("nao")
