#4 - Peça ao usuário para digitar dois números e imprima se ambos são positivos.

nmr = float(input('digite seu primeiro número aqui: '))
nmr2 = float(input('digite seu segundo número: '))

if nmr > 0 and nmr2 > 0:
    print('ambos números positivos')
elif nmr > 0 and nmr2 < 0:
    print('um dos seus números são negativos')
else:
    print('seus números são negativos')