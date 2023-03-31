"""
Desafio 010a

ENUNCIADO: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
dólares ela pode comprar, considerando que U$1,00 = R$3,27.
"""
money = float(input('Quanto de dinheiro você tem? R$'))
conv = money / 3.27
print(f'\nCom R${money:.2f} você pode comprar US${conv:.2f}, no máximo.')
