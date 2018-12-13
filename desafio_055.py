#!/usr/local/bin/python3

'''
Faça um programa que leia o peso de cinco pessoas. No final,
mostre qual foi o maior e o menor peso lidos.
'''
# pega a data atual
# from datetime import date
# atual = date.today().year

# Cria uma lista vazia
quilo = []

for pes in range(1, 6):
    peso = float(input('Peso da {}ª pessoa:  '.format(pes)))

# Caso o peso for maior que zero, adiciona na lista
    if peso > 0:
        quilo.append(peso)
    else:
        print('Valor invalido !!!')

print('O maior peso lido foi de {0:.2f} Kg'.format(max(quilo)))
print('O menor peso lido foi de {0:.2f} Kg'.format(min(quilo)))
print('\nA soma de todos os pesos é {0:.2f} Kg'.format(sum(quilo)))
