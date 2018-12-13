#!/usr/local/bin/python3

'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''

print('Vamos criar uma PA...')

termo = int(input('Digite o termo da PA: '))
razao = int(input('Digite a razão da PA: '))
pa = 10

for c in range(termo,razao):
    print(c)