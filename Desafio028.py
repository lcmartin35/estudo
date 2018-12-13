print(' ===  Desafio 028  ===\n')


print(' Jogo da Adivinhação v1.0')
print("""
Escreva um programa que faça o computador "pensar" em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
escolhido pelo computador. O programa deverá escrever na tela se o usuário
venceu ou perdeu.

\n""")

from random import randint
num = randint(0,5)

while True:
    usuario = int(input('Digite um numero de 0 a 5:  '))



    if usuario == num:
        print('PARABÉNS !!!!Você acertou!!!!')
        break     

    else:
        print('ERROU!!! tente outra vez...! ')
    

    
