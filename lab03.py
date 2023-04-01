# Daniel de Sousa cipriano RA: 233228
# Programa que leia a altura e diâmetro de um tanque de combustivel e calcule o volume, indicando quais postos poderão ser abastecidos de acordo com a capacidade de cada um.

#Entradas

d = float(input())
h = float(input())
pA = float(input())
pB = float(input())
pC = float(input())

 #Cálculo do volume do cilindro
v = 3.14 * ((d/2)**2) * h

#Conversão de m³ para L
v = v*1000

if v >= pA:
    print("posto A foi reabastecido")
    v = v - pA
else:
    print("posto A nao foi reabastecido")
if v >= pB:
    print("posto B foi reabastecido")
    v = v - pB
else:
    print("posto B nao foi reabastecido")
if v >= pC:
    print("posto C foi reabastecido")
else:
    print("posto C nao foi reabastecido")
