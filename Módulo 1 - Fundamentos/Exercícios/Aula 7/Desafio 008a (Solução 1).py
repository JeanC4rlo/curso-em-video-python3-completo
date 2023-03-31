"""
Desafio 008a (Solução 1)

ENUNCIADO: Escreva um programa que leia um valor em metros e exiba convertido em centímetros e em
milímetros.
"""
medida = float(input('Insira o valor em metros: '))
cm = medida * 100
mm = cm * 10
print(f'Em {medida} metros temos {cm} centímetros e {mm} milímetros.')
