import random

print(' ===  Desafio 019  ===\n')
 
"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo
na tela o nome do escolhido.

FORMULA: 

"""
print('   Sorteando um item da Lista \n\n')

aluno1 = input('Digite o 1° nome :')
aluno2 = input('Digite o 2° nome :')
aluno3 = input('Digite o 3° nome :')
aluno4 = input('Digite o 4° nome :')

lista = [aluno1, aluno2, aluno3, aluno4]


sorteio = random.choice(lista)
print('\n\nO aluno Sorteado foi: {}'.format(sorteio))
