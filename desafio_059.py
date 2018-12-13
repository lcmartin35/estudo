#!/usr/bin/python3
'''
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
maior = []
print('''
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
opcao = int(input('Qual é a sua Opção? '))
while opcao != 5:
        
    if opcao == 1:
        soma = v1 + v2
        print('A soma entre {} + {} é {}'.format(v1, v2, soma))
        print('-=-==-==-==-==-==-==-==-=-')
    elif opcao == 2:
        mult = v1 * v2
        print('O resultado de {} x {} é {}'.format(v1, v2, mult))
        print('-=-==-==-==-==-==-==-==-==-=-')
    elif opcao == 3:
        maior.append(v1)
        maior.append(v2)
        print('Entre {} e {} o maior valor é {}'.format(v1, v2, max(maior)))
        print('-=-==-==-==-==-==-==-==-==-==-==-=-')