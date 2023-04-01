# Daniel de Sousa Cipriano RA: 233228

def triangular(a):
	soma = 0
	for x in range(1,a+1):
		soma += x
		if soma == a:
			return True
			break
		elif (soma != a) and (x == a):
			return False
			break
def perfeito(b):
	soma = 0
	for y in range(1,b):
		if b % y == 0:
			soma += y
	if soma == b:
		return True
	else:
		return False


rounds = pointsryu = pointsken = 0
while rounds != 2:
	rounds += 1
	pvryu = pvken = 2000
	golpesneg = golpespos = 0
	while (pvryu + golpesneg > 0) and (pvken + golpespos > 0):
		golpe = (int(input()))
		cond1 = True
		cond2 = True
		if golpe > 0:
			cond1 = triangular(golpe)
			cond2 = perfeito(golpe)
		else:
			cond1 = triangular(-golpe)
			cond2 = perfeito(-golpe)
		if cond1 == True and cond2 == True:
			golpe *= 3
		elif cond1 == True and cond2 == False:
			golpe *= 2
		elif cond1 == False and cond2 == True:
			golpe *= 3

		if golpe > 0 and golpesneg != 0:
			print('Ryu: {} - {} = {}'.format(pvryu, -golpesneg, (pvryu + golpesneg)))
			pvryu += golpesneg
			golpesneg = 0
		if golpe < 0 and golpespos != 0:
			print('Ken: {} - {} = {}'.format(pvken, -golpespos, (pvken + golpespos)))
			pvken += golpespos
			golpespos = 0
		if golpe < 0 and ((pvryu + golpesneg) > 0):
			golpesneg += golpe
		elif golpe > 0 and ((pvken + golpespos) > 0):
			golpespos -= golpe
	if (pvryu + golpesneg > 0):
		print('Ken: {} - {} = {}'.format(pvken, -golpespos, (pvken + golpespos)))
		pointsryu += 1
	elif (pvken + golpespos > 0):
		print('Ryu: {} - {} = {}'.format(pvryu, -golpesneg, (pvryu + golpesneg)))
		pointsken += 1
	if pointsryu == 2:
		print('Ryu venceu')
	elif pointsken == 2:
		print('Ken venceu')
	elif pointsryu == pointsken:
		print('empatou')
