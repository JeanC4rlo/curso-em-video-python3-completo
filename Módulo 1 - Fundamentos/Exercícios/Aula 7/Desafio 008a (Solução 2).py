"""
Desafio 008a (Solução 2)

ENUNCIADO: Escreva um programa que leia um valor em metros e exiba convertido em centímetros e em
milímetros.
"""
medida = float(input('Insira o valor em metros: '))
cm = medida * 100
mm = medida * 1000
print(f'Em {medida} metros temos {cm} centímetros e {mm} milímetros.')
