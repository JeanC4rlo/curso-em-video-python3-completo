"""
Desafio 004 (Solução 1)

ENUNCIADO: Faça um programa que leia algo que foi enviado no terminal e mostre na tela seu tipo
primitivo e todas as informações possíveis sobre ele.
"""
value = input('Digite algo: ')
num = value.isnumeric()
alpha = value.isalpha()
alphanum = value.isalnum()
american = value.isascii()
digit = value.isdigit()
decimal = value.isdecimal()
pyId = value.isidentifier()
lower = value.islower()
upper = value.isupper()
printable = value.isprintable()
space = value.isspace()
title = value.istitle()
print(f'\n{type(value)}\n'
      f'O valor contém apenas números? {num}'
      f'O valor contém apenas letras? {alpha}'
      f'O valor contém apenas letras e/ou números? {alphanum}'
      f'O valor contém apenas caracteres ASCII? {american}'
      f'O valor contém apenas dígitos? {digit}'
      f'O valor contém apenas caracteres decimais? {decimal}'
      f'O valor é um identificador Python válido? {pyId}'
      f'O valor contém apenas caracteres minúsculos? {lower}'
      f'O valor contém apenas caracteres maiúsculos? {upper}'
      f'O valor contém apenas caracteres válidos para serem exibidos? {printable}'
      f'O valor é um caractere vazio? {space}'
      f'O valor está capitalizado? {title}')
