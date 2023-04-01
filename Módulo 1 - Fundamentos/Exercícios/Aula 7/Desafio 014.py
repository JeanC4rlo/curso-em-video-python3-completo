"""
Desafio 014

ENUNCIADO: Escreva um programa que converta uma temperatura digitada em °C para °F.
DICA: Use a fórmula "F = ((C * 9) / 5) + 32" ou "F = (1,8 * C) + 32"
"""
c = float(input('Insira uma temperatura em ºC: '))
f = (c * 1.8) + 32
print(f'\n{c}ºC equivalem à {f}ºF.')
