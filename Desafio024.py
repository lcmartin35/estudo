print(' ===  Desafio 024  ===\n')


print('Separando dígitos de um número')
print("""
Crie um programa que leia o nome de uma cidade diga se ela começa
ou não com o nome "SANTO".

\n""")

cidade = str(input('Digite o nome de Uma cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')

