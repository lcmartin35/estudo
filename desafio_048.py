#!/usr/local/bin/python3

'''
Faça um programa que calcule a soma entre todos os números que são 
múltiplos de três e que se encontram no intervalo de 1 até 500.
'''
s = 0
for c in range(1, 500, 3):
    print(c)
    s += c 
print('A soma do intervalo é {}'.format(s))
