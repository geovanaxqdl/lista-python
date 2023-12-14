#Escreva um programa que, dados dois números inteiros,
#mostre na tela o maior deles.

nmr = int(input('digite um número: '))
nmr2 = int(input('digite o segundo número: '))

if nmr > nmr2:
    print(f'{nmr} é maior que {nmr2} a diferença foi de:', nmr - nmr2,'números')
elif nmr < nmr2:
    print(f'{nmr2} é maior que {nmr} a diferença foi de:', nmr2 - nmr,'números')
else:
    print('os dois números são iguais')
