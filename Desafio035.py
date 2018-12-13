
print(' ===  Desafio 041  ===\n')


print('        Analisando Triângulo v1.0 \n\n')
"""
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: 
- EQUILÁTERO: todos os lados iguais 
- ISÓSCELES: dois lados iguais, um diferente 
- ESCALENO: todos os lados diferentes

REGRA:
cada medida tem que ser menor que a soma de duas outras medidas:

"""
a = int(input('Digite a primeira reta: '))
b = int(input('Digite a segunda reta: '))
c = int(input('Digite a terceira reta: '))

if a < b + c and b < a + c and c < a + b:
    print('\nPode ser contruido um triangulo !!')
else:
    print('\033[1;31mNÃO\033[m poderá ser contruido um triangulo')
