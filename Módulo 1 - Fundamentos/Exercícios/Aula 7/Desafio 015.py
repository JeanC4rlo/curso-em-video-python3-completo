"""
Desafio 015

ENUNCIADO: Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a
quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa
R$60,00 por dia e R$0,15 por km rodado.
"""
dias = int(input('Insira a quantidade de dias que você alugou o carro: '))
km = float(input('Insira quantos km você rodou: '))
p_dias = dias * 60
p_km = km * 0.15
total = p_dias + p_km
print(f'\n'
      f'Você alugou o carro por {dias} dias e rodou {km:.2f}km, '
      f'você vai pagar R${p_dias:.2f} pelo tempo de aluguel e R${p_km:.2f} pelos km rodadados, '
      f'totalizando R${total:.2f}.')
