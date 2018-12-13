#!/usr/bin/python3
from random import randint
print(' ===  Desafio 058  ===\n')
print(' Jogo da Adivinhação v2.0')
'''
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número
entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
'''
tentativas = 0
num = randint(0, 10)
print('''Sou seu computador...
Acabei de pensar em um numero entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
palp = int(input('\nQual seu papite? '))
while palp != num:
    if palp > num:
        palp = int(input('Menos... Tente mais uma vez. '))
        tentativas += 1
    elif palp < num:
        palp = int(input('Mais... Tente mais uma vez. '))
        tentativas += 1
    elif palp == num:
        break
print('Acertou com {} tentativas. Parabéns! '.format(tentativas))
