"""
Desafio 010b

ENUNCIADO: Escreva um programa que leia um valor em reais e converta para dólares, euros e ienes,
considerando que U$1,00 = R$5,16, 1,00 € = R$5,55 e ¥1,00 = R$0,039.
"""
real = float(input('Quanto de dinheiro você tem? R$'))
dol = real / 5.16
euro = real / 5.55
iene = real / 0.039
print(f'\nCom R${real:.2f}, você pode comprar:\n'
      f'\nUS${dol:.2f}'
      f'\n¥{iene:.3f}'
      f'\n{euro:.2f} €')
