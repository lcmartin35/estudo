
print(' ===  Desafio 033  ===\n')


print('              Ano Bissexto \n\n')
"""
 Faça um programa que leia três numeros e mostre quel é o maior
 e qual é o menor.

"""

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro Valor: '))

# Verificando quem é menor

menor = a

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Verificando quem é maior

maior = a

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
