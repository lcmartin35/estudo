import math

print(' ===  Desafio 018  ===\n')
 
"""
Faça um programa que leia um ângulo qualquer
e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

FORMULA: 

"""
print('   Seno, Cosseno e Tangente \n\n')

angulo = float(input('Digite um angulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
                

print('O ângulo de {} tem o SENO de :{:.2f}\n'.format(angulo, seno))
print('O ângulo de {} tem o COSSENO de :{:.2f}\n'.format(angulo, cosseno))
print('O ângulo de {} tem a TANGENTE  de :{:.2f}\n'.format(angulo, tangente))
