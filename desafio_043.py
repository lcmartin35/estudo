#!/usr/local/bin/python3

'''
Desenvolva um programa que leia seis números inteiros e mostre a soma
apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''
s = 0
for c in range(0,6):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        s += num
    else:
        pass
print('A somatoria dos numeros pares é {}'.format(s))
