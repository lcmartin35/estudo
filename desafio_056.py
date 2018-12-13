#!/usr/local/bin/python3

'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome
do homem mais velho e quantas mulheres têm menos de 20 anos.
'''
# Solução professor Guanabra
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A medida de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))











'''
#solucao Luiz em 11/12/2018
# Cria uma lista vazia
nomes_mulher = []
idades_mulher = []
sexos_mulher = []
nomes_homem = []
idades_homem = []
sexos_homem = []

for pess in range(1, 3):
    print('\n---- {}ª PESSOA ----  '.format(pess))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    if sexo == 'm' or sexo == 'M':
        nomes_homem.append(nome)
        idades_homem.append(idade)
        sexos_homem.append(sexo)
    elif sexo == 'f' or sexo == 'F':
        nomes_mulher.append(nome)
        idades_mulher.append(idade)
        sexos_mulher.append(sexo)
media = sum(idades_homem + idades_mulher) / 4
print('A média de idade do grupo é de  {0:.1f} anos'.format(media))
print('O home mais velho tem {} anos e se chama {} '.format(max(idades_homem)))
# print('\nA soma de todos os pesos é {0:.2f} Kg'.format(sum(quilo)))
'''