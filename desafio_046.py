#!/usr/local/bin/python3

'''
Faça um programa que mostre na tela uma contagem regressiva para o estouro
de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''
from time import sleep

print('Atenção para a queima de Fogos!! ')
print('Contando...')

for c in range (10, 0, -1):
    sleep(1)
    print(c)

print('FELIZ 2019 !!!!!')

