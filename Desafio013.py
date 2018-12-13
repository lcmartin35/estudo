print(' ===  Desafio 013  ===\n')
 
"""
Faça um algoritmo que leia o salário de um funcionário
e mostre seu novo salário, com 15% de aumento.


FORMULA: salario * reajuste /100 + salario

"""
print('   Reajuste Salarial \n\n')

salario = float(input('Digite o valor de seu salario :R$ '))
reajuste = 15
vd = salario * reajuste  / 100
vf = salario + vd
print('Você terá um reajuste de 15% \n')
print('Seu novo salario será de R$ {:.2f} Reais'.format(vf))

                

