"""
Desafio 004 (Solução 2)

ENUNCIADO: Faça um programa que leia algo que foi enviado no terminal e mostre na tela seu tipo
primitivo e todas as informações possíveis sobre ele.
"""
value = input('Digite algo: ')
print(f'\n{type(value)}\n')
print(f'O valor contém apenas números? {value.isnumeric}')
print(f'O valor contém apenas letras? {value.isalpha}')
print(f'O valor contém apenas letras e/ou números? {value.isalnum}')
print(f'O valor contém apenas caracteres ASCII? {value.isascii}')
print(f'O valor contém apenas dígitos? {value.isdigit}')
print(f'O valor é um identificador Python válido? {value.isidentifier}')
print(f'O valor contém apenas caracteres minúsculos? {value.islower}')
print(f'O valor contém apenas caracteres maiúsculos? {value.isupper}')
print(f'O valor contém apenas caracteres válidos para serem exibidos? {value.isprintable}')
print(f'O valor é um caractere valido? {value.isspace}')
print(f'O valor está captalizado? {value.istitle}')
