print(' === Desafio 008 ===')

"""
Escreva um programa que leia um valor em metros e o
exiba convertido em centímetros e milímetros.

"""
print('Conversor de metros para centimetros e milimetros\n')

metros = int(input('Entre com o valor em metros:'))

print('Você digitou {} metros'.format(metros))

print('{} metros equivale a {} centrimetros'.format(metros, metros * 100))
print('{} metros equivale a {} milimetros'.format(metros, metros * 1000))



