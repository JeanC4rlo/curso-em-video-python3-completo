"""
Desafio 012

ENUNCIADO: Faça um algoritmo que leia o preço de um produto e mostre um novo preço com 5% de
desconto.
"""
p_inicial = float(input('Insira o preço de um produto: R$'))
p_final = p_inicial - (p_inicial * (1 / 20))
print(f'\nUm produto de R${p_inicial:.2f} com 5% de desconto fica por R${p_final:.2f}.')
