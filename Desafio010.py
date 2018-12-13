print(' ===  Desafio 010  ===')
 
"""
 Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
 mostre quantos dólares ela pode comprar.
 
"""
print('     Conversor de Moedas')
 
carteira = float(input('Digite o quanto você possui em sua Carteira :'))

print('Você Possui R$ {} você pode comprar $ {:.2f} Dolares'.format(carteira, carteira / 3.27))
print('Arredondando $ {} Dolares'.format(carteira // 3.27))




