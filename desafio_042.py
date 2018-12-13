#!/usr/local/bin/python3

'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, 
mostre quantas pessoas ainda não atingiram a maioridade e 
quantas já são maiores.
'''
pessoa = 1
for c in range(0,7):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoa)))
    pessoa += 1
if nasc >= 18:
    maior = nasc
else:
    menor = nasc
    