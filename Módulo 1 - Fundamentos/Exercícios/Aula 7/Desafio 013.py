"""
Desafio 013

ENUNCIADO: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15%
de aumento.
"""
salario = float(input('Qual é o seu salário atual? '))
aumento = (salario / 100) * 15
novo_salario = salario + aumento
print(f'Seu salário com 15% de aumento será de R${novo_salario}.')
