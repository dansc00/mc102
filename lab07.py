# Daniel de Sousa Cipriano RA: 233228

rounds = pointsryu = pointsken = 0
while rounds != 2:
	rounds += 1
	pvryu = pvken = 50
	golpesneg = golpespos = 0
	while (pvryu + golpesneg > 0) and (pvken + golpespos > 0):
		golpe = (int(input()))
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
