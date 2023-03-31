"""
Desafio 008b (Solução 1)

ENUNCIADO: Escreva um programa que converta uma medida em metros para quilômetros, hectômetros,
decâmetros, decímetros, centímetros e milímetros.
"""
medida = float(input('Insira uma medida em metros: '))
km = medida / 1000
hm = km * 10
dam = hm * 10
dm = medida * 10
cm = dm * 10
mm = cm * 10
print(f'{medida}m equivale a:\n'
      f'\n{km}km'
      f'\n{hm}hm'
      f'\n{dam}dam'
      f'\n{dm}dm'
      f'\n{cm}cm'
      f'\n{mm}mm')
