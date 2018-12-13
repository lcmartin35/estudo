from math import hypot

print(' ===  Desafio 017  ===\n')
 
"""
Faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.

FORMULA: a² + b² = c²

"""
print('   Catetos e Hipotenusa \n\n')

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

print('O valor da hipotenusa é {:.2f}'.format(hypot(num1, num2)))

