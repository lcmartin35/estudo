print(' ===  Desafio 031  ===\n')


print('Custo da Viagem')
"""
 Desenvolva um programa que pergunte a distância de uma viagem em Km.
 Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
 e R$0,45 parta viagens mais longas.

"""


num = int(input('Qual a distancia da vigem em Km ? : '))

if num  <= 200:
    print('O valor de sua passagem é de R$ {:.2f} '.format(num * 0.50))
else:
    print('O valor de sua passagem é de R$ {:.2f} '.format(num * 0.45))

