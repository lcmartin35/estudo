print(' === Desafio 009 ===')

"""
Faça um programa que leia um número Inteiro qualquer e
mostre na tela a sua tabuada.

"""
print('TABUADA')

t = int(input('Entre com um numero para saber sua tabuada:'))

for i in range(11):
    print('{} x {}',i , '= {}'.format(t, t * i))
    


