#Daniel de Sousa Cipriano RA: 233228
# Calcular o tempo em que deve ocorrer a ativação de um micro explosivo que desviará uma bomba para um certa distância.


h = float(input())
vb = float(input())
d = float(input())
T = float(input())

# Cálculo do tempo total de queda

ttq = h/vb
tb = d/T
ta = ttq-tb
print("{:.3f}".format(ta))
