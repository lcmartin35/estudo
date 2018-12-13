print(' ===  Desafio 029  ===\n')


print(' Radar Eletrônico')
print("""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.

\n""")

vel_max = 80

vel_carro = int(input('Qual a velocidade de seu carro ?: '))

if vel_carro <= vel_max:
    print('Ok ! Você esta dentro do limite de velocidade!')

else:
    print('Você foi multado!! Seu carro estava a {} Km\h'.format(vel_carro))
    multa = (vel_carro - vel_max) * 7.00
    print('O valor da sua multa sera de R$ {:.2f}'.format(multa))


