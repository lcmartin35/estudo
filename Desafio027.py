print(' ===  Desafio 027  ===\n')


print('Primeiro e último nome')
print("""
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
\n""")

nome = str(input('Digite seu nome completo: ')).strip().upper()

dividido = nome.split()

print('O primeiro nome é : {} '.format(dividido[0]))

print('O ultimo nome é : {} '.format(dividido[-1]))

