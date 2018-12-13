#!/usr/local/bin/python3

'''
Faça um programa que leia um número inteiro
e diga se ele é ou não um número primo.
'''
num = int(input('Digite um numero: '))

if num % 2 == 0:
    print('O numero {} NÃO é primo'.format(num))
else:
    print('O numero {} É primo'.format(num))