"""
Desafio 004 (Solução 1)

ENUNCIADO: Faça um programa que leia algo que foi enviado no terminal e mostre na tela seu tipo
primitivo e todas as informações possíveis sobre ele.
"""
value = input('Digite algo: ')
num = value.isnumeric()
alpha = value.isalpha()
alphanum = value.isalnum()
ascii = value.isascii()
digit = value.isdigit()
decimal = value.isdecimal()
pyId = value.isidentifier()
lower = value.islower()
upper = value.isupper()
printable = value.isprintable()
space = value.isspace()
title = value.istitle()

print(f'\n{type(value)}\n')
print(f'O valor contém apenas números? {num}')
print(f'O valor contém apenas letras? {alpha}')
print(f'O valor contém apenas letras e/ou números? {alphanum}')
print(f'O valor contém apenas caracteres ASCII? {ascii}')
print(f'O valor contém apenas dígitos? {digit}')
print(f'O valor contém apenas caracteres decimais? {decimal}')
print(f'O valor é um identificador Python válido? {pyId}')
print(f'O valor contém apenas caracteres minúsculos? {lower}')
print(f'O valor contém apenas caracteres maiúsculos? {upper}')
print(f'O valor contém apenas caracteres válidos para serem exibidos? {printable}')
print(f'O valor é um caractere vazio? {space}')
print(f'O valor está capitalizado? {title}')
