print(' ===  Desafio 026  ===\n')


print('Primeira e última ocorrência')
print("""
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes
aparece a letra "A", em que posição ela aparece a primeira vez e em que
posição ela aparece a última vez.
\n""")

frase = str(input('Digite uma frase: ')).strip().upper()


print('A letra "A" aparece {} vezes'.format(frase.count('A')))
print('A primeira posicão é  {} e a ultima é {}'.format(frase.find('A'),frase.rfind('A')))

