# Calcular o total a ser pago por uma corrida de aplicativo. Utilizando uma taxa por distância pecorrida e outra fixa.
# Daniel de Sousa Cipriano RA: 233228

# Entradas

vi = int(input())
xi = int(input())
yi = int(input())
xf = int(input())
yf = int(input())
t = int(input())

# Cálculo da distância

dist= (xf - xi) + (yf - yi)

# Cálculo do valor total

tot = vi + (dist*t)
print(tot)
