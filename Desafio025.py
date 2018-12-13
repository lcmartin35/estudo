print(' ===  Desafio 025  ===\n')


print('Procurando String')
print("""
Crie um programa que leia o nome de uma pessoa e diga
se ela tem "SILVA" no nome.
\n""")

nome = str(input('Digite oseu  nome completo: ')).strip()


print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))

