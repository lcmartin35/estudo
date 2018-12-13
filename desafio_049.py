#!/usr/local/bin/python3

'''
Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.
'''
from time import sleep
num = int(input('Escolha a tabuada:  '))

print('\nVocê escolheu a tabuada do numero: {}'.format(num))
print('Aguarde... montando a tabuada...\n')
sleep(2)
print('Pronto!!') 
for c in range(0,11):
    print('{} x {} = {}'.format(num, c , num * c ))