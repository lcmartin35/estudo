print(' ===  Desafio 030  ===\n')


print('Par ou Ímpar')
"""
 Crie um programa que leia um número inteiro e mostre na tela
 se ele é PAR ou ÍMPAR.

"""


num = int(input('Digite um numero inteiro: '))

resultado = num % 2
if resultado == 0:
    print('O numero {} é PAR'.format(num))
else:
    print('O numero {} é IMPAR'.format(num))
          
