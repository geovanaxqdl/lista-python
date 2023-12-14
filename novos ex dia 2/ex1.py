#1 - Faça um algoritmo que converta uma temperatura em graus Celsius para Fahrenheit. Isso envolve a aplicação da fórmula correta de conversão.
#multiplicar a temperatura em graus Celsius por 1,8 e somar 32.

temp = int(input('digite quantos graus está: '))

calc = (temp*1.8) + 32
print(f'sua temperatura em Fahrenheit é: {calc}')