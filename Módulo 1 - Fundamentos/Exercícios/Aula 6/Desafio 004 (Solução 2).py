"""
Desafio 004 (Solução 2)

ENUNCIADO: Faça um programa que leia algo que foi enviado no terminal e mostre na tela seu tipo
primitivo e todas as informações possíveis sobre ele.
"""
value = input('Digite algo: ')
print(f'\n{type(value)}\n'
      f'O valor contém apenas números? {value.isnumeric}'
      f'O valor contém apenas letras? {value.isalpha}'
      f'O valor contém apenas letras e/ou números? {value.isalnum}'
      f'O valor contém apenas caracteres ASCII? {value.isascii}'
      f'O valor contém apenas dígitos? {value.isdigit}'
      f'O valor é um identificador Python válido? {value.isidentifier}'
      f'O valor contém apenas caracteres minúsculos? {value.islower}'
      f'O valor contém apenas caracteres maiúsculos? {value.isupper}'
      f'O valor contém apenas caracteres válidos para serem exibidos? {value.isprintable}'
      f'O valor é um caractere valido? {value.isspace}'
      f'O valor está captalizado? {value.istitle}')
