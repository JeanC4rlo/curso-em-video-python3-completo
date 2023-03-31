"""
Desafio 011 (Solução 1)

ENUNCIADO: Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua 
área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma
área de 2m².
"""
lar = float(input('Insira a largura da parede em metros: '))
alt = float(input('Insira a altura da parede em metros: '))
area = lar * alt
tinta = area / 2
print(f'\nA área da parede é de {area}m², você precisa de {tinta} litros de tinta para pintá-la completamente.')
