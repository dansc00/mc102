char = (input().upper().split())
for x in char:
    if x == 'MERCURIO':
        print('N - ', end='')
    elif x == 'VENUS':
        print('NE - ', end='')
    elif x == 'TERRA':
        print('L - ', end='')
    elif x == 'MARTE':
        print('SE - ', end='')
    elif x == 'JUPITER':
        print('S - ', end='')
    elif x == 'SATURNO':
        print('SO - ', end='')
    elif x == 'URANO':
        print('O - ', end='')
    elif x == 'NETUNO':
        print('NO - ', end='')
    elif x == 'VERDE':
        print('30')
    elif x == 'AMARELO':
        print('45')
    elif x == 'VERMELHO':
        print('60')
