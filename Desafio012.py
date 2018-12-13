print(' ===  Desafio 012  ===\n')
 
"""
Faça um algoritmo que leia o preço de um produto e
mostre seu novo preço, com 5% de desconto.

FORMULA: valor * desconto /100

"""
print('    Calculando Descontos\n\n')

produto = float(input('Digite o preço do produto :R$ '))
vd = produto * 5 / 100
vf = produto - vd
print('O valor do produto com de desconto de 5% é R$ {:.2f}'.format(vf))

                

