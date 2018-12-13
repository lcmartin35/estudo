print(' ===  Desafio 015  ===\n')
 
"""
Escreva um programa que pergunte a quantidade de Km percorridos
por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar,
sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

FORMULA: 

"""
print('    Aluguel de carros \n\n')

km_rodado = int(input('Digite a quantidade de Km percorridos :'))
dias_alugado = int(input('Qual a quantidade de dias alugado ?:'))
vf = (km_rodado * 0.15) + (dias_alugado * 60)

print('O preço a Pagar pelo veiculo é R$ {:.2f}'.format(vf))


