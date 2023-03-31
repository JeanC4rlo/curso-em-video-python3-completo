"""
Desafio 008b (Solução 2)

ENUNCIADO: Escreva um programa que converta uma medida em metros para quilômetros, hectômetros,
decâmetros, decímetros, centímetros e milímetros
"""
medida = float(input('Insira uma medida em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print(f'{medida}m equivale a:\n'
      f'\n{km}km'
      f'\n{hm}hm'
      f'\n{dam}dam'
      f'\n{dm}dm'
      f'\n{cm}cm'
      f'\n{mm}mm')
