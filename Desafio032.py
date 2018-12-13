
print(' ===  Desafio 032  ===\n')


print('              Ano Bissexto \n\n')
"""
 Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

"""
from datetime import date

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O Ano de {} é BISSEXTO '.format(ano))
else:
    print('O Ano de {} NÃO é BISSEXTO '.format(ano))

