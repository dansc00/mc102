# Daniel de Sousa Cipriano RA: 233228

d = int(input())
emp = emptot = []
for x in range(0,(d*4)):
    emp.append(float(input())) # adiciona os valores de acões em uma lista
emptot = [emp[0:d],emp[d:2*d],emp[2*d:3*d],emp[3*d:4*d]] #Fatia a lista emp, separando as acões para cada empresa
minimo = 0
for z in range(0,4): # Adiciona o valor mínimo, ou seja, a acão que mais compensa no dia.
    if z == 0:
        minimo = emptot[z[0]] - emptot[z[d-1]]
    elif z != 0:
        if (emptot[z[0]] - emptot[z[d-1]]) < minimo:
            minimo = (emptot[z[0]] - emptot[z[d-1]])
